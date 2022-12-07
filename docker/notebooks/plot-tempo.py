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


tempo_data = []
tempo_idx = []
tempo_stats = []
tempo_mean = []
for i in range(0, len(keys)):
    if i not in outliers_idx:
        key = list(reversed(keys))[i]
        tempo = d[key][1][1]
        tempo_data.append(tempo[0])
        tempo_stats.append([np.mean(tempo), np.std(tempo), np.median(tempo)])
        tempo_mean.append(np.mean(tempo))
        tempo_idx.append(i)

img_pwd = "../img"
os.chdir(img_pwd)
print("Working directory:", os.getcwd())

plt.figure(figsize=(12, 5))
# the histogram of the data
plt.subplot(121)
n, bins, patches = plt.hist(tempo_data, bins=10, alpha=0.95)
plt.xlabel("Tempo", fontsize=18)
plt.ylabel("Counts", fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
# plt.title('Distribution of tempos', fontsize=22)
plt.grid(True, linestyle=":", linewidth=0.5)
plt.subplot(122)
plt.boxplot(tempo_data)
# plt.xlabel('Counts', fontsize=18)
plt.ylabel("Tempo", fontsize=18)
plt.xticks([])
plt.yticks(fontsize=14)
plt.grid(True, linestyle=":", linewidth=0.5)
plt.suptitle("Distribution of tempos", fontsize=22)
plt.tight_layout()
plt.savefig("plot-tempo-hist-box.jpg")
