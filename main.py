import whisper
# get system args
import sys
import moviepy.editor as mp
import argparse

parser = argparse.ArgumentParser(prog = 'AI Captions', description = 'Create captions for videos using AI.')
parser.add_argument("-v", "--video", help="The video file to add captions to", required=True, type=str)
parser.add_argument("-m", "--model", help="The whisper model to use", required=True, type=str)
parser.add_argument("-p", "--preview", help="Preview the video", action="store_true")

args = parser.parse_args()

video = None
clips = []

def main():
    global video
    videoFile = args.video
    whisperModel = args.model
    # get audio from video usinng mp
    video = mp.VideoFileClip(videoFile)
    audio = video.audio
    audio.write_audiofile("output/audio.mp3")
    # send audio to whisper
    model = whisper.load_model(whisperModel)
    out = model.transcribe("output/audio.mp3", verbose=True)
    addCaptions(out)
    
def addCaptions(output):
    global video
    global clips
    # loop through all segments
    lastEnd = None
    for segment in output["segments"]:

        start = segment["start"]
        end = segment["end"]

        if end > video.audio.duration:
            end = video.audio.duration
        text = segment["text"]
        clip = video.subclip(start, end)
        if lastEnd is not None:
            if lastEnd != start:
                clipWithNoCaptiom = video.subclip(lastEnd, start)
                clips.append(clipWithNoCaptiom)
        text_clip = mp.TextClip(text, color='white', method="label", size=clip.size, interline=-1, kerning=-2, align="South").set_duration(clip.duration)
        clip = mp.CompositeVideoClip([clip, text_clip])
        clips.append(clip)
        lastEnd = end
    video = mp.concatenate_videoclips(clips)
    video.write_videofile("output/output.mp4")
    if args.preview:
        newVideo = mp.VideoFileClip("output/output.mp4")
        newVideo.preview(fps=newVideo.fps)

def validateArgs():
    if args.video is None:
        print("You must provide a video file")
        sys.exit()
    if args.model is None:
        print("You must provide a whisper model")
        sys.exit()


if __name__ == "__main__":
    main()