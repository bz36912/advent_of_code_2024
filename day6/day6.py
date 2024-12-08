import numpy as np
file = open("day6/input.txt", "r")

text = file.read()
numCol = text.index("\n")
oriMap = np.zeros((numCol, numCol), dtype=str)
for x in range(numCol):
    for y in range(numCol):
        oriMap[y, x] = text[y * (numCol + 1) + x]

print(oriMap)
DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
SYMBOL = ["^", ">", "v", "<"]

def find_path(map, newOb = None):
    foundLoop = False
    loc = np.where(map=='^')
    guardY, guardX = loc[0][0], loc[1][0]
    direction = UP # (x, y)=(0,-1), sinceinitially the guard goes upwards
    step = 0
    while True:
        if step > 20000:
            foundLoop = True
            break
        if guardX < 0 or guardX >= numCol or guardY < 0 or guardY >= numCol:
            break
        
        if step != 0:
            if map[guardY, guardX] == SYMBOL[direction]:
                # infinite loop is detected.
                foundLoop = True
                break
        step += 1
        map[guardY, guardX] = SYMBOL[direction] # marks the area searched
        frontX, frontY = guardX + DIRECTIONS[direction][0], guardY + DIRECTIONS[direction][1]
        if frontX < 0 or frontX >= numCol or frontY < 0 or frontY >= numCol:
            direction = (direction + 1) % len(DIRECTIONS) # turn right
            break
        if map[frontY, frontX] == '#': # obstacle is blocking the way
            direction = (direction + 1) % len(DIRECTIONS) # turn right
            continue
        else:
            guardX, guardY = frontX, frontY
    return foundLoop

tempMap = oriMap.copy()
find_path(tempMap)
print(tempMap)
pathX, pathY = [], []
for s in SYMBOL:
    pathX.extend(list(np.where(tempMap==s)[1]))
    pathY.extend(list(np.where(tempMap==s)[0]))
print(f"areas searched: {len(pathX)}")

# part 2
numPossiblePos = 0
loc = np.where(oriMap=='^')
initGuardY, initGuardX = loc[0][0], loc[1][0]
for i in range(len(pathX)):
    addX, addY = pathX[i], pathY[i]
    tempMap = oriMap.copy()
    if addX == initGuardX and addY == initGuardY:
        continue # cannot place new obstacles at the location of the guard's starting point
    tempMap[addY, addX ] = "#"
    foundLoop = find_path(tempMap, newOb = (addY, addX))
    if foundLoop:
        print(f"place at {(addY, addX)}")
        numPossiblePos += 1

print(f"numPossiblePos: {numPossiblePos}")
print("end")