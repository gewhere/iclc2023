import itertools
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib as mpl
from os import listdir
from os.path import isfile, join
import os
import pickle
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from matplotlib import ticker

os.chdir("../data/")
os.getcwd()
data_fn = "algorave10-feature-extraction.pkl"
# load data
with open(data_fn, "rb") as handle:
    d = pickle.load(handle)
# performance list
with open("performances.pkl", "rb") as handle:
    performances = pickle.load(handle)
# load list with outliers
with open("outliers_idx.pkl", "rb") as handle:
    outliers_idx = pickle.load(handle)
# inverse keys to match performances
keys = list(reversed(sorted(list(d.keys()))))


def rosette_seg(x, N):
    segment_len = np.array_split(x, N)
    segment_div = []
    for elem in segment_len:
        segment_div.append(np.mean(elem))
    return np.array(segment_div)


# DATA for plotting
name = d[keys[-1]][0][0]
val_oenv = d[keys[-1]][0][1]
val_centroid = d[keys[-1]][4][1].reshape(-1)

# FIGURE
os.chdir("../img/")
print(os.getcwd())
N = 72
width = 2 * np.pi / N
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = rosette_seg(val_oenv, N)  # oenv
slice_color = rosette_seg(val_centroid, N)  # oenv


# COLORBAR
def colored_bar(left, height, z=None, width=0.8, bottom=0, ax=None, **kwargs):
    if ax is None:
        ax = plt.gca()
    width = itertools.cycle(np.atleast_1d(width))
    bottom = itertools.cycle(np.atleast_1d(bottom))
    rects = []
    for x, y, h, w in zip(left, bottom, height, width):
        rects.append(Rectangle((x, y), w, h))
    coll = PatchCollection(rects, array=z, **kwargs)
    ax.add_collection(coll)
    ax.xaxis.set_major_formatter(ticker.PercentFormatter(2 * np.pi, decimals=1))
    #     ax.autoscale()
    ax.set_rmax(np.max(radii))
    return coll


# FIGURE
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="polar")
x_theta = np.radians(np.arange(0, 360, 5))
y = radii  # radius of the polar plot
z = slice_color  # mapped to colorbar
cmap = plt.get_cmap("viridis")
coll = colored_bar(x_theta, y, z, ax=ax, width=np.radians(5), cmap=cmap)
cbar = fig.colorbar(coll, pad=0.08)
cbar.ax.tick_params(labelsize=14)
cbar.ax.set_ylabel("Hz", rotation=270, fontsize=15, labelpad=25)
ax.set_yticks([0.25, 0.5, 0.75, 1.0, 1.25, 1.5])
ax.tick_params(axis="both", which="major", labelsize=14)
plt.title("Onsets strength and spectral centroid", fontsize=18)
plt.savefig("polar-template-circular-plot.jpg")
