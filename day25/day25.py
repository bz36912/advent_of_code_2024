import numpy as np
file1 = open("day25/input.txt")
text = file1.read()
elems = text.split("\n\n")

NUM_PINS = 5
locks = []
keys = []
for elem in elems:
    if elem[0] == "#": # it is a lock
        heights = [-1,] * NUM_PINS
        for i, c in enumerate(elem):
            if c == "#":
                heights[i % (NUM_PINS+1)] += 1
        locks.append(np.array(heights))
    else: # it is a key
        heights = [6,] * NUM_PINS
        for i, c in enumerate(elem):
            if c == ".":
                heights[i % (NUM_PINS+1)] -= 1
        keys.append(np.array(heights))

# print(locks)
# print(keys)

numMatches = 0
for i, lock in enumerate(locks):
    for j, key in enumerate(keys):
        if np.all(lock + key <= 5):
            numMatches += 1

print(f"numMatches: {numMatches}")
print("end")