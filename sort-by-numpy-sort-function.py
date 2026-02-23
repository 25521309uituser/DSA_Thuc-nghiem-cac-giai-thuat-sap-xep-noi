import time
import numpy

lists = []

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f: 
        arr = list(map(float, line.split()))
        lists.append(arr)

cnt = [] * 10

for arr in lists:
    start = time.perf_counter()
    arr.sort()
    end = time.perf_counter()
    cnt.append(int((end - start) * 1000))

print(cnt)