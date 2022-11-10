import whisper
from whisper.utils import write_vtt
import subprocess
import os
# get system args
import argparse

parser = argparse.ArgumentParser(prog = 'AI Captions', description = 'Create captions for videos using AI.')
parser.add_argument("-v", "--video", help="The video file to add captions to", required=True, type=str)
parser.add_argument("-m", "--model", help="The whisper model to use", required=True, type=str)
parser.add_argument("-p", "--preview", help="Preview the video", action="store_true")

args = parser.parse_args()

def main():
    videoFile = args.video
    whisperModel = args.model
    validateVideo(videoFile)
    print("Extracting audio from video")
    subprocess.call("ffmpeg -i " + videoFile + " output/audio.mp3 -y -hide_banner -v warning -stats")
    # get audio from video usinng mp
    # send audio to whisper
    model = whisper.load_model(whisperModel)
    print("Transcribing audio")
    out = model.transcribe("output/audio.mp3", verbose=True)
    with open("output/captions.vtt", "w") as f:
        print("Writing transcript to file")
        write_vtt(out["segments"], file=f)
        addCaptions()
    
def addCaptions():
    print("Adding captions to video")
    subprocess.call("ffmpeg -i " + args.video + " -vf subtitles=output/captions.vtt output/output.mp4 -y -hide_banner -v warning -stats")
    if args.preview:
        print("Previewing video")
        # get absolute path
        path = os.path.abspath("output/output.mp4")
        os.startfile(path)


def validateVideo(videoFile):
    # check if video file exists
    try:
        with open(videoFile, 'r') as f:
            pass
    except FileNotFoundError:
        print("Video file does not exist")
        exit()

if __name__ == "__main__":
    main()