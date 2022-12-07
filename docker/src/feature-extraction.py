import librosa
import os
from os import listdir
from os.path import isfile, join
from moviepy.editor import *
import pickle
import time
import re

print('===============================================')
print('========== FEATURE EXTRACTION SCRIPT ==========')
print('===============================================')
t = time.time()

mypath = "/data/algorave10-large-files/mp3"  # '/Users/geodia/data/algorave/algorave10/mp3' # <path of mp3 files>
onlyfiles = [f for f in listdir(mypath) if (isfile(join(mypath, f)) and "mp3" in f)]

pattern = "([0-9]{2}\-[A-Za-z]{3}\-[2]{2}\-[0-9]{2}\-[0-9]{2})"

data = dict()

hop_length = 512

for i in range(0, len(onlyfiles)):
    print(i, '-', onlyfiles[i])
    try:
        m = re.search(pattern, onlyfiles[i])
        timetag = m.group(0)
        print(f"{str(i+1)} / {len(onlyfiles)} -- timetag: {timetag}")
        data[timetag] = timetag
    except:
        print(i, '>>> EXCEPTION: ', onlyfiles[i])
        print('isfile:', isfile(onlyfiles[i]))
        print('stats:', os.stat(onlyfiles[i]))
        print('getSize:', os.path.getsize(onlyfiles[i]))
        # Fix performances with no timetag in the URL
        pattern = "([02]{4}\-[0-9]{2}\-[0-9]{2}\s[0-9]{2}\:[0-9]{2})"
        m = re.search(pattern, onlyfiles[i])
        timetag = m.group(0)
        timetag = timetag[8:10] + '-Mar-' + timetag[2:4] + '-' + timetag[-5:-3] + '-' + timetag[-2:]
    # Compute local onset autocorrelation
    y, sr = librosa.load(mypath + "/" + onlyfiles[i])
    # TEMPORAL FEATURES
    oenv = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop_length)
    tempo = librosa.beat.tempo(onset_envelope=oenv, sr=sr)
    pulse = librosa.beat.plp(onset_envelope=oenv, sr=sr)
    # # SPECTRAL FEEATURES
    # mfcc = librosa.feature.mfcc(y=y, sr=sr)
    # centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
    # rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr, roll_percent=0.95)
    # flatness = librosa.feature.spectral_flatness(y=y)
    # spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    # contrast = librosa.feature.spectral_contrast(y=y, sr=sr)
    # pitch = librosa.pyin(y, fmin=65, fmax=2093)  # CPU EXPENSIVE !!
    # dict
    data[timetag] = [
        ("oenv", oenv),
        ("tempo", tempo),
        ("pulse", pulse),
        # ("mfcc", mfcc),
        # ("centroid", centroid),
        # ("rolloff", rolloff),
        # ("flatness", flatness),
        # ("spec_bw", spec_bw),
        # ("contrast", contrast),
        # ("pitch", pitch),
    ]


print(os.getcwd())  # print working dir
# os.chdir("/Users/geodia/submissions/ISMIR2022/docker/data")
os.chdir("/data")
print(os.getcwd())  # print working dir


with open("algorave10-feature-extraction.pkl", "wb") as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

elapsed = time.time() - t
print("Elapsed time:", elapsed)
