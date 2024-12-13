import numpy as np
from queue import Queue

DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))
def climb(startX, startY, map):
    peaks = []
    toSearch = Queue()
    toSearch.put((startX, startY))
    while not toSearch.empty():
        searchX, searchY = toSearch.get()
        height = map[searchY, searchX]
        for dir in DIRECTIONS:
            newX, newY = searchX + dir[0], searchY + dir[1]
            if newX < 0 or newX >= map.shape[1] or newY < 0 or newY >= map.shape[0]:
                continue
            if map[newY, newX] == height + 1:
                if map[newY, newX] == 9:
                    peaks.append((newX, newY))
                else:
                    toSearch.put((newX, newY))
    
    score = len(peaks)
    print(f"score at {(startX, startY)} is {score}")
    return score

file = open("day10/dummy.txt", "r")
text = file.read()
numCol = text.index("\n")
oriMap = np.zeros((numCol, numCol), dtype=int)
for x in range(numCol):
    for y in range(numCol):
        val = text[y * (numCol + 1) + x]
        if val == '.':
            val = -1
        oriMap[y, x] = int(val)

loc = np.where(oriMap==0)
headY, headX = loc[0], loc[1]

total = 0
for i in range(len(headX)):
    total += climb(headX[i], headY[i], oriMap)

print(f"total: {total}")
print("end")