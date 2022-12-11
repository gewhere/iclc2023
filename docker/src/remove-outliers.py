import numpy as np
import pickle
import os

data_fn = "algorave10-feature-extraction.pkl"
pwd_root = ""
data_pwd = "/data"

print(os.getcwd())  # print working dir
os.chdir(pwd_root + data_pwd)
print('data_pwd:', os.getcwd())  #

with open(data_fn, "rb") as handle:
    d = pickle.load(handle)

with open("performances.pkl", "rb") as handle:
    performances = pickle.load(handle)

keys = sorted(list(d.keys()))

# print whether a performance started on time
for i in range(0, len(keys)):
    dd = list(reversed(keys))[i][:2]
    hh = list(reversed(keys))[i][10:12]
    mm = list(reversed(keys))[i][13:15]
    timeslot_reconstructed = "2022-03-" + dd + " " + hh + ":" + mm
    timeslot_true = performances[i][1]
    if timeslot_reconstructed == timeslot_true:
        print(i, ": TRUE -- ", performances[i][0])
    else:
        print(i, ": FALSE -- ", performances[i][0])


# collect indices of delayed performances
outliers_delayed = []
for i in range(0, len(keys)):
    dd = list(reversed(keys))[i][:2]
    hh = list(reversed(keys))[i][10:12]
    mm = list(reversed(keys))[i][13:15]
    timeslot_reconstructed = "2022-03-" + dd + " " + hh + ":" + mm
    timeslot_true = performances[i][1]
    if timeslot_reconstructed != timeslot_true:
        print(i, ": FALSE -- ", performances[i][0], " -- ", timeslot_reconstructed)
        data_len = d[list(reversed(keys))[i]][0][1].shape[0]
        print(data_len)
        outliers_delayed.append(i)

# exclude performances with no sound
outliers_nosound = []
for i in range(0, len(keys)):
    key = list(reversed(keys))[i]
    data = d[key]
    oenv = data[0][1]
    oenv_mean = np.mean(oenv)
    if oenv_mean < 0.3:
        print(i, oenv_mean)
        outliers_nosound.append(i)

outliers_idx = sorted(list(set(outliers_delayed).union(set(outliers_nosound))))
print("Total number of outliers:", len(outliers_idx))
print("Outlier index lis:", outliers_idx)

os.chdir(data_pwd)
print(os.getcwd())  # print working dir

with open("outliers_idx.pkl", "wb") as handle:
    pickle.dump(outliers_idx, handle, protocol=pickle.HIGHEST_PROTOCOL)
