import random

n = 1000000
filename = "data.txt"

def write_float_sequence(f, data):
    f.write(" ".join(f"{x:.6f}" for x in data))
    f.write("\n")

def write_int_sequence(f, data):
    f.write(" ".join(str(x) for x in data))
    f.write("\n")

with open(filename, "w", encoding="utf-8") as f:
    arr = [random.uniform(0, 1000000) for _ in range(n)]
    arr.sort()
    write_float_sequence(f, arr)

    arr = [random.uniform(0, 1000000) for _ in range(n)]
    arr.sort(reverse=True)
    write_float_sequence(f, arr)

    for _ in range(3):
        arr = [random.uniform(0, 1000000) for _ in range(n)]
        write_float_sequence(f, arr)

    for _ in range(5):
        arr = [random.randint(0, 1000000) for _ in range(n)]
        write_int_sequence(f, arr)
