import time

def quicksort(arr, l, r):
    i = l
    j = r
    mid = (l + r) // 2
    while (i < j):
        while (arr[i] < arr[mid]):
            i += 1
        while (arr[j] > arr[mid]):
            j -= 1
        if (i <= j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if (i < r):
        quicksort(arr, i, r)
    if (l < j):
        quicksort(arr, l, j)

lists = []

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f: 
        arr = list(map(float, line.split()))
        lists.append(arr)

cnt = [] * 10

for arr in lists:
    start = time.perf_counter()
    quicksort(arr, 0, len(arr) - 1)
    end = time.perf_counter()
    cnt.append(int((end - start) * 1000))

print(cnt)
