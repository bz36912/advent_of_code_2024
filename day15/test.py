import numpy as np
import sys
from queue import Queue
np.set_printoptions(threshold=sys.maxsize)

file = open("day15/correct_dummy_p2.txt", "r")
text = file.read()
numCol = text.index("\n")
oriMap = np.zeros((numCol // 2, numCol), dtype=str)
robX, robY = None, None
for y in range(numCol // 2):
    for x in range(numCol):
        oriMap[y, x] = text[y * (numCol + 1) + x]

print(oriMap)
obstacles = np.where(oriMap == "[")
gps = np.sum(100 * obstacles[0] + obstacles[1])
print(f"gps: {gps}")
print("end")