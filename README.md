[![GitHub issues](https://img.shields.io/github/issues/godmoded/ai-captions?style=for-the-badge)](https://github.com/godmoded/ai-captions/issues)
[![GitHub forks](https://img.shields.io/github/forks/godmoded/ai-captions?style=for-the-badge)](https://github.com/godmoded/ai-captions/network)
[![GitHub stars](https://img.shields.io/github/stars/godmoded/ai-captions?style=for-the-badge)](https://github.com/godmoded/ai-captions/stargazers)
[![GitHub license](https://img.shields.io/github/license/godmoded/ai-captions?style=for-the-badge)](https://github.com/GodModed/ai-captions/blob/master/LICENSE)

# Ai Captions

Create captions for videos using AI.

## Description

This small project uses OpenAI's whisper AI to generate captions for videos.

## Getting Started

### Dependencies

* FFmpeg
* Python

### Installing

* Clone the repo
* Install python from [here](https://www.python.org/downloads/) if you have not already installed it.
* You can install FFmpeg from [here](https://www.ffmpeg.org/download.html) or use your package manager to install it.
* Install the requirements by running `py setup.py` inside of the project directory.

### Executing program

* If you have not already, run the `setup.py` file to install the required packages.
```bash
python setup.py
```
* Then run the `main.py` with your own arguments.
```bash
python main.py -v <video path> -m <whisper model name> -p (-p is optional)
```

* Example
```bash
python main.py -v video.mp4 -m tiny.en -p
```

* Arguments
    * `-v` or `--video` - The path to the video file.
    * `-m` or `--model` - The name of the model to use. (The list of models can be found below)
    * `-p` or `--preview` - If you want to preview the generated video.

* Models

|  Size  | Parameters | English-only model | Multilingual model | Required VRAM | Relative speed |
|:------:|:----------:|:------------------:|:------------------:|:-------------:|:--------------:|
|  tiny  |    39 M    |     `tiny.en`      |       `tiny`       |     ~1 GB     |      ~32x      |
|  base  |    74 M    |     `base.en`      |       `base`       |     ~1 GB     |      ~16x      |
| small  |   244 M    |     `small.en`     |      `small`       |     ~2 GB     |      ~6x       |
| medium |   769 M    |    `medium.en`     |      `medium`      |     ~5 GB     |      ~2x       |
| large  |   1550 M   |        N/A         |      `large`       |    ~10 GB     |       1x       |

For English-only applications, the .en models tend to perform better, especially for the tiny.en and base.en models.
These models are provided by OpenAI. [More Info](https://github.com/openai/whisper/blob/main/README.md)

It may take some time to run for the first time since the AI model needs to be downloaded.

The output of the program will be in the `output` folder. There will be a video called `output.mp4` inside of the folder. There will also be a transcript file called `captions.vtt` and an audio file called `audio.mp3`.
## Help

Make an [Issue](https://github.com/GodModed/ai-captions/issues) to report a bug or request a feature.

## Authors

[@GodModed](https://github.com/GodModed)

## Version History

* 0.2
    * Added the ability to preview the generated video.
    * Added better argument parsing.
* 0.1.1
   * Fixed video getting cut off
* 0.1.0
    * Initial Release

## License

This project is licensed under the [GNU General Public License v3.0](https://github.com/GodModed/ai-captions/blob/main/LICENSE) License.

## Acknowledgments

* [Nicholas Renotte](https://www.youtube.com/watch?v=_xVTgdpokH4)
* [OpenAI Whisper](https://github.com/openai/whisper)
