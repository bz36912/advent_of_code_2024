import numpy as np

file = open("day15/inputMap.txt", "r")
text = file.read()
numCol = text.index("\n")
oriMap = np.zeros((numCol, numCol), dtype=str)
for x in range(numCol):
    for y in range(numCol):
        val = text[y * (numCol + 1) + x]
        oriMap[y, x] = val

loc = np.where(oriMap=='@')
robY, robX = int(loc[0][0]), int(loc[1][0])
# print(oriMap)
oriMap[robY, robX] = "." # to remove the @

DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
SYMBOL = ["^", ">", "v", "<"]
file = open("day15/input.txt", "r")
text = file.read()
for c in text:
    if c == "": # end of file
        break
    if c == "\n":
        continue
    direction = None
    for i, sym in enumerate(SYMBOL):
        if sym == c:
            direction = DIRECTIONS[i]
            testX, testY = robX + direction[0], robY + direction[1]
    
    if oriMap[testY, testX] == ".": # empty spot
        robX, robY = testX, testY
    elif oriMap[testY, testX] == "#": # immoveable wall
        pass # do nothing
    elif oriMap[testY, testX] == "O":
        nextX, nextY = testX, testY
        while True:
            nextX += direction[0]
            nextY += direction[1]
            if oriMap[nextY, nextX] == "#":
                break # robot do nothing
            if oriMap[nextY, nextX] == ".":
                # shift the boxes
                oriMap[nextY, nextX] = "O"
                oriMap[testY, testX] = "."
                robX, robY = testX, testY # move the robot
                break

# print(oriMap)
obstacles = np.where(oriMap == "O")
gps = np.sum(100 * obstacles[0] + obstacles[1])
print(f"gps: {gps}")
print("end")