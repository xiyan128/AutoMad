# AutoMad
DSSQ Anime Music Video generator. Not for serious use.

## Installation

Prerequisite: Anaconda
1. Clone this repo
2. run `conda env create -f environment.yml` and then activate the environment

## Usage

In the project directory:
```python
from lib import MadDump

# input videos: could be any composite clip, variable length
# audio: the music file upon which we perform beats detection 
dump = MadDump("input1.mp4", "input2.mp4", audio="test.mp3")

# parse the composite video into separate scenes
dump.find_all_scenes()

# composite the video by concatenating parsed scenes and adding background music
dump.export("out.mp4")

# upload the output file to video streaming sites
```

## Dependencies

Three major dependencies are
1. Scenedetect - to parse composite videos into separate ones
2. Aubio - to detect beats in the music
3. Moviepy - to concatenate video clips

## Disclaimer
This project does not intend to serve as a means of production but rather a parody of the prevalent 大势所趋(DSSQ) videos 
on BiliBili.

License: GNU GPL