import numpy as np
from queue import Queue

DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
SYMBOL = ["^", ">", "v", "<"]
def explore(startX, startY, map, destX, destY, allowCheat=True, fixedCost=None):
    toSearch = Queue()
    cost = np.full_like(map, dtype=float, fill_value=np.inf)
    cost[startY, startX] = 0
    toSearch.put((startX, startY))

    while not toSearch.empty():
        (searchX, searchY) = toSearch.get()
        searchCost = cost[searchY, searchX]
        if (searchX, searchY) == (destX, destY):
            break
        for i, dir in enumerate(DIRECTIONS):
            newX, newY = searchX + dir[0], searchY + dir[1]
            if newX < 0 or newX >= map.shape[1] or newY < 0 or newY >= map.shape[0]:
                continue
            if map[newY, newX] == "#":
                continue # has already cheated and cannot cheat again
            
            newCost = searchCost
            newCost += 1

            if cost[newY, newX] < newCost:
                continue
                
            cost[newY, newX] = newCost
            toSearch.put((newX, newY))
    
    return cost

file = open("day20/input.txt", "r")
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
cost = explore(robX, robY, oriMap, destX, destY, allowCheat=False)
print(f"the cost reach E: {cost[destY, destX]}")

def calculate_improvement(cost1, cost2, reducedCosts, fasterBy100, offset=2):
    if cost1 != np.inf and cost2 != np.inf:
        improvement = abs(cost1 - cost2) - offset
        if improvement >= 50:
            if improvement not in reducedCosts:
                reducedCosts[improvement] = 0
            reducedCosts[improvement] += 1

        if improvement >= 100:
            fasterBy100 += 1
    return reducedCosts, fasterBy100
reducedCosts = {}
fasterBy100 = 0

# # Part 1
# for x in range(1, numCol - 1):
#     for y in range(1, numCol - 1):
#         if oriMap[y, x] != "#":
#             continue

#         # check vertical shortcut
#         upCost = cost[y+DIRECTIONS[UP][1], x+DIRECTIONS[UP][0]]
#         downCost = cost[y+DIRECTIONS[DOWN][1], x+DIRECTIONS[DOWN][0]]
#         reducedCosts, fasterBy100 = calculate_improvement(upCost, downCost, reducedCosts, fasterBy100)

#         # check horizontal shortcut
#         leftCost = cost[y+DIRECTIONS[LEFT][1], x+DIRECTIONS[LEFT][0]]
#         rightCost = cost[y+DIRECTIONS[RIGHT][1], x+DIRECTIONS[RIGHT][0]]
#         reducedCosts, fasterBy100 = calculate_improvement(leftCost, rightCost, reducedCosts, fasterBy100)

y, x = np.where(cost != np.inf)
deltaY = np.abs(y.reshape(1, -1) - y.reshape(-1, 1))
deltaX = np.abs(x.reshape(1, -1) - x.reshape(-1, 1))
delta = deltaX + deltaY
index1, index2 = np.where(delta <= 20)

for i in range(len(index1)):
    if index2[i] >= index1[i]:
        continue
    cost1 = cost[y[index1[i]], x[index1[i]]]
    cost2 = cost[y[index2[i]], x[index2[i]]]
    offset = delta[index1[i], index2[i]]
    reducedCosts, fasterBy100 = calculate_improvement(cost1, cost2, reducedCosts, fasterBy100, offset=offset)

print(f"reducedCosts: {reducedCosts}")
print(f"fastBy100: {fasterBy100}")
print("end")