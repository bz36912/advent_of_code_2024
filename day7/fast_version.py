import numpy as np
from time import time

startTime = time()
total = 0
file = open("day7/input.txt", "r")
for aline in file:
    parts = aline.split(":")
    target = int(parts[0])
    operator = parts[1].strip().split(" ")
    operator = [int(op) for op in operator]

    possibilities = np.zeros(3**(len(operator)-1), dtype=int)
    possibilities[0] = operator[0]
    for i in range(len(operator)-1):
        cursor = 3**i
        inputs = possibilities[:cursor]
        possibilities[cursor:cursor*2] = inputs * operator[i+1]
        for j in range(cursor):
            possibilities[cursor*2 + j] = int(str(inputs[j]) + str(operator[i+1]))
        possibilities[:cursor] += operator[i+1]

    if np.sum(possibilities == target) != 0:
        total += target
        print(f"{aline.strip()}")

print(f"total: {total}, after {time()-startTime} seconds")
print("end")

# with input.txt and 3 operator, the correct answer should be 340362529351427
# it took 36.279677867889404 seconds