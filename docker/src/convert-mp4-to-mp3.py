import os
from os import listdir
from os.path import isfile, join
from moviepy.editor import *

mypath = "/"  # why not a cmd line arg? '<THE MP4 PATH HERE>' # ./data/mp4 ?
# better only consider files with ending .mp4
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and "mp4" in f)]

# PATH TO STORE MP3 ./data/mp3 ?
for elem in onlyfiles:
    video = VideoFileClip(elem)
    video.audio.write_audiofile(elem[:-4] + ".mp3")
