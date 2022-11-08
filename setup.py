# import whisper
import subprocess
# import moviepy.editor as mp
# download these imports

print("Installing dependencies")

subprocess.run(["pip", "install", "git+https://github.com/openai/whisper.git"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print("You may need to install ffmpeg if you don't have it already")
