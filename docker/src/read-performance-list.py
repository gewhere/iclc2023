import os
import pickle

fn = "algorave10-performance-list.org"
pwd_root = ""

print(os.getcwd())  # print working dir
os.chdir(pwd_root + "/data")
print(os.getcwd())  # print working dir

with open(fn) as file:
    read_data = file.read()

data_arr = read_data.splitlines()
str_list = list(filter(None, data_arr))
performances_total_num = len(str_list) / 8, len(str_list)

# print perfmormance list as a string
for i in range(0, len(str_list)):
    if i % 8 == 0:
        print(i, str_list[i])

# store performances and metadata in a python list
header_str = "Algorave 10th Birthday March 2022 live performance by "
performances = []
for i in range(0, int(len(str_list) / 8)):
    wd = str_list[i * 8].split(" - ")[1:]
    who = wd[0]
    date = wd[1]
    url = str_list[(i * 8) + 1].split("-")[1].lstrip()
    dl_url = str_list[(i * 8) + 2].split("- ")[1].lstrip()
    tmp = str_list[(i * 8) + 5].replace(header_str, "")
    tmp = tmp.replace(who, "")
    place = tmp.replace(" from ", "")
    title = str_list[(i * 8) + 6]
    performances.append((who, date, url, dl_url, place, title))

# print(performances, len(performances))

# OUTPUT FILE
fn_url = "url-performances-algorave-10.txt"

with open(fn_url, "a") as file:
    # CHECK IF FILE IS EMPTY !!
    if os.stat(fn_url).st_size != 0:
        # EMPTY FILE
        f = open(fn_url, "r+")
        f.truncate(0)
    for elem in performances:
        # print URL of the performances from the Internet Archive
        print(elem[3])
        file.write(elem[3] + "\n")

with open("performances.pkl", "wb") as handle:
    pickle.dump(performances, handle, protocol=pickle.HIGHEST_PROTOCOL)
