import numpy as np
from queue import Queue
DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))
WIDTH = 71
def explore(oriMap):
    toSearch = Queue()
    toSearch.put([(0, 0), 0])
    cost = np.full_like(oriMap, dtype=float, fill_value=np.inf)
    cost[0, 0] = 0

    while not toSearch.empty():
        (searchX, searchY), searchCost = toSearch.get()
        oriMap[searchY, searchX] = "O"
        for i, dir in enumerate(DIRECTIONS):
            newX, newY = searchX + dir[0], searchY + dir[1]
            if newX < 0 or newX >= oriMap.shape[1] or newY < 0 or newY >= oriMap.shape[0]:
                continue
            if oriMap[newY, newX] == "#":
                continue
            newCost = searchCost + 1
            if newCost < cost[newY, newX]:
                cost[newY, newX] = newCost
                toSearch.put([(newX, newY), newCost])
    
    return cost[WIDTH-1, WIDTH-1] != np.inf # if the end is reachable

def add_obstacles(obstacles):
    oriMap = np.full((WIDTH, WIDTH), ".", dtype=str) # clear old obstacles
    for ob in obstacles:
        oriMap[ob[1], ob[0]] = "#"
    return oriMap

file = open("day18/input.txt", "r")
text = file.read()
coordinates = text.split("\n")
coordinates = [eval(f"({coord})") for coord in coordinates]

area = len(coordinates) // 2
pt = len(coordinates) // 2
while area > 1:
    oriMap = add_obstacles(coordinates[:pt])
    area = (area + 1) // 2
    if explore(oriMap):
        print(f"reachable when pt = {pt}")
        pt += area
    else:
        print(f"UNreachable when pt = {pt}")
        pt -= area

print(f"coordinates[:3030][-1]: {coordinates[:3030][-1]}")

# for pt in range(3027, 3031):
#     oriMap = add_obstacles(coordinates[:pt])
#     if explore(oriMap):
#         print(f"reachable when pt = {pt}")
#     else:
#         print(f"UNreachable when pt = {pt}")
print("end")