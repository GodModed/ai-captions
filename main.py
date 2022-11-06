import whisper
# get system args
import sys
import moviepy.editor as mp

video = None
clips = []

def getArgs(index):
    if len(sys.argv) > index:
        return sys.argv[index]
    else:
        return None

def main():
    global video
    validateArgs()
    videoFile = getArgs(1)
    whisperModel = getArgs(2)
    # get audio from video usinng mp
    video = mp.VideoFileClip(videoFile)
    audio = video.audio
    audio.write_audiofile("output/audio.mp3")
    # send audio to whisper
    model = whisper.load_model(whisperModel)
    out = model.transcribe("output/audio.mp3")
    getData(out)

def validateArgs():
    if getArgs(1) is None:
        print("Please provide a video file\nUsage: py main.py <video file> <whisper model>")
        sys.exit()
    if getArgs(2) is None:
        print("Provide a whisper model\nUsage: py main.py <video file> <whisper model>")
        sys.exit()

def getData(output):

    global video
    
    length = video.audio.duration

    addCaptions(output)
    
    # loop through all segments
    for segment in output["segments"]:
        # get start and end time
        start = segment["start"]
        end = segment["end"]
        # get text
        text = segment["text"]

        if end > length:
            end = length

        # export audio
        # get length of audio
        print(f"[{start}-{end}] {text}")
    
def addCaptions(output):
    global video
    global clips
    # loop through all segments
    for segment in output["segments"]:
        start = segment["start"]
        end = segment["end"]
        if end > video.audio.duration:
            end = video.audio.duration
        text = segment["text"]
        clip = video.subclip(start, end)
        text_clip = mp.TextClip(text, color='white', method="label", size=clip.size, interline=-1, kerning=-2, align="South").set_duration(clip.duration)
        clip = mp.CompositeVideoClip([clip, text_clip])
        clips.append(clip)
    video = mp.concatenate_videoclips(clips)
    video.write_videofile("output/output.mp4")


if __name__ == "__main__":
    main()