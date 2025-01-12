import numpy as np
from queue import Queue

MAX_COST = 114476  #  11048 7036

DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
SYMBOL = ["^", ">", "v", "<"]
def explore(startX, startY, map):
    toSearch = Queue()
    cost = np.full_like(map, dtype=float, fill_value=np.inf)
    toSearch.put((startX, startY))
    cost[startY, startX] = 0
    map[startY, startX] = ">"

    while not toSearch.empty():
        searchX, searchY = toSearch.get()
        searchCost = cost[searchY, searchX]
        for i, dir in enumerate(DIRECTIONS):
            newX, newY = searchX + dir[0], searchY + dir[1]
            if newX < 0 or newX >= map.shape[1] or newY < 0 or newY >= map.shape[0]:
                continue
            if map[newY, newX] == "#":
                continue
            
            newCost = searchCost
            if map[searchY, searchX] != SYMBOL[i]: # there is a turn
                newCost += 1000
            newCost += 1

            if cost[newY, newX] < newCost:
                continue
            
            cost[newY, newX] = newCost
            map[newY, newX] = SYMBOL[i]
            toSearch.put((newX, newY))
       
    return cost

partOfBestPath = []
def explore_part2(startX, startY, map, destX, destY):
    toSearch = Queue()
    toSearch.put([(startX, startY), [], 0, DIRECTIONS[RIGHT]])
    map[startY, startX] = ">"
    cost = np.full_like(map, dtype=float, fill_value=np.inf)
    cost[startY, startX] = 0

    skips = 0 # input.txt: 3347
    numSearch = 0 # input.txt has 44,000 searches
    while not toSearch.empty():
        (searchX, searchY), path, searchCost, lastDir = toSearch.get()
        numSearch += 1
        if (searchX, searchY) == (destX, destY):
            partOfBestPath.extend(path)
            partOfBestPath.append((destX, destY))
            continue

        for i, dir in enumerate(DIRECTIONS):
            newX, newY = searchX + dir[0], searchY + dir[1]
            if newX < 0 or newX >= map.shape[1] or newY < 0 or newY >= map.shape[0]:
                continue
            if map[newY, newX] == "#":
                continue
            if (newX, newY) in path: # cycle detected
                continue
            
            newCost = searchCost
            if lastDir != dir: # there is a turn
                newCost += 1000
            newCost += 1

            if newCost > cost[newY, newX] + 1000:
                skips += 1
                continue
            if newCost < cost[newY, newX]:
                cost[newY, newX] = newCost

            if searchCost > MAX_COST or searchCost % 1000 > MAX_COST % 1000:
                continue

            map[newY, newX] = SYMBOL[i]
            newPath = path.copy()
            newPath.append((searchX, searchY))
            toSearch.put([(newX, newY), newPath, newCost, dir])
       
    return -1

file = open("day16/input.txt", "r")
text = file.read()
numCol = text.index("\n")
oriMap = np.zeros((numCol, numCol), dtype=str)
for x in range(numCol):
    for y in range(numCol):
        val = text[y * (numCol + 1) + x]
        oriMap[y, x] = val

loc = np.where(oriMap=='S')
robY, robX = int(loc[0][0]), int(loc[1][0])
dest = np.where(oriMap=='E')
destY, destX = int(dest[0][0]), int(dest[1][0])
cost = explore_part2(robX, robY, oriMap, destX, destY)

print(f"the cost reach E: {cost[destY, destX]}")
print("end")

# part 2: 477 is too low