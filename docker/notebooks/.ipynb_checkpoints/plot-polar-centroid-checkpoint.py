import matplotlib.pyplot as plt
import numpy as np
import pickle
import os

data_pwd = "../data"
os.chdir(data_pwd)
print("Working directory:", os.getcwd())

# load extracted features
data_fn = "algorave10-feature-extraction.pkl"
with open(data_fn, "rb") as handle:
    d = pickle.load(handle)
keys = sorted(list(d.keys()))

# load list of performances
with open("performances.pkl", "rb") as handle:
    performances = pickle.load(handle)

# load list with outliers
with open("outliers_idx.pkl", "rb") as handle:
    outliers_idx = pickle.load(handle)

# get spectral centroid data
centroid_data = []
centroid_idx = []
centroid_sim = []
for i in range(0, len(keys)):
    if i not in outliers_idx:
        key = list(reversed(keys))[i]
        data = d[key][4]  #  centroid
        centroid = data[1].reshape(-1)
        centroid_data.append(centroid)
        centroid_idx.append(i)

N = 72
plt.figure(figsize=(36, 36))
# ignore true divide
np.seterr(divide="ignore", invalid="ignore")
j = 0
for i in range(0, len(keys)):
    if i not in outliers_idx:
        # select idx from j
        # x = np.array(d[keys[j]][4][1]).reshape(-1) # centroid
        x = centroid_data[j]
        segment_len = np.array_split(x, N)
        segment_div = []
        for elem in segment_len:
            segment_div.append(np.mean(elem))
        theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
        radii = np.array(segment_div)
        width = 2 * np.pi / N
        colors = plt.cm.viridis(radii / np.max(radii))
        # plt
        plt.subplot(11, 11, j + 1, projection="polar")
        plt.bar(theta, radii, width=width, bottom=0.0, color=colors, alpha=0.95)
        # plt.title(str(j), fontsize=16)
        plt.title(str(i) + ": " + performances[i][0], fontsize=16)
        j = j + 1

plt.tight_layout()

img_pwd = "../img"
os.chdir(img_pwd)
print("Working directory:", os.getcwd())
plt.savefig("polar-centroid-121-performances.jpg")
