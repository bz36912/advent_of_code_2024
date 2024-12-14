import numpy as np
from queue import Queue

DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))
def expand(startX, startY, map, marked):
    toSearch = Queue()
    toSearch.put((startX, startY))
    marked[startY, startX] = True
    key = map[startY, startX]
    area = 1
    perimeter = 0

    surrounds = np.zeros_like(marked)
    while not toSearch.empty():
        searchX, searchY = toSearch.get()
        for dir in DIRECTIONS:
            newX, newY = searchX + dir[0], searchY + dir[1]
            if newX < 0 or newX >= map.shape[1] or newY < 0 or newY >= map.shape[0]:
                perimeter += 1
                continue
            if map[newY, newX] != key:
                perimeter += 1
                surrounds[newY, newX] = True
            elif not marked[newY, newX]:
                area += 1
                toSearch.put((newX, newY))
                marked[newY, newX] = True
    
    
    print(f"key {key} has area:{area}, perimeter:{perimeter}, cost:{area*perimeter}")
    return area, perimeter, surrounds

file = open("day12/dummy.txt", "r")
text = file.read()
numCol = text.index("\n")
oriMap = np.zeros((numCol, numCol), dtype=str)
marked = np.zeros((numCol, numCol), dtype=bool)
for x in range(numCol):
    for y in range(numCol):
        val = text[y * (numCol + 1) + x]
        oriMap[y, x] = val

totalCost = 0
for x in range(numCol):
    for y in range(numCol):
        if marked[y, x]:
            continue
        area, perimeter, surrounds = expand(x, y, oriMap, marked)
        sY, sX = np.where(surrounds == True)

        numSides = 0
        marked2 = np.zeros((numCol, numCol), dtype=bool)
        for i in range(len(sX)):
            if marked2[sY[i], sX[i]]:
                continue
            expand(sX[i], sY[i], surrounds, marked2) # updates marked2
            numSides += 1
        totalCost += area * numSides

print(f"cost: {totalCost}")
print("end")