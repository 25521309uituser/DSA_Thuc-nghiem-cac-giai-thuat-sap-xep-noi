import time

def mergesort(arr):
    temp = [0] * len(arr)
    _mergesort(arr, temp, 0, len(arr) - 1)

def _mergesort(arr, temp, left, right):
    if left < right:
        mid = (left + right) // 2
        _mergesort(arr, temp, left, mid)
        _mergesort(arr, temp, mid + 1, right)
        merge(arr, temp, left, mid, right)

def merge(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

lists = []

with open("data.txt", "r", encoding="utf-8") as f:
    for line in f: 
        arr = list(map(float, line.split()))
        lists.append(arr)

cnt = [] * 10

for arr in lists:
    start = time.perf_counter()
    mergesort(arr)
    end = time.perf_counter()
    cnt.append(int((end - start) * 1000))

print(cnt)