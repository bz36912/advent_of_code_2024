import numpy as np
import sys
from queue import Queue
np.set_printoptions(threshold=sys.maxsize)

file = open("day15/inputMap.txt", "r")
text = file.read()
numCol = text.index("\n")
oriMap = np.zeros((numCol, numCol * 2), dtype=str)
robX, robY = None, None
for y in range(numCol):
    for x in range(numCol):
        val = text[y * (numCol + 1) + x]
        if val == '@':
            robX, robY = 2*x, y
            val = '.' # so I can simplify and don't need to consider '@' later in the code.
        if val == 'O':
            oriMap[y, 2*x] = "["
            oriMap[y, 2*x + 1] = "]"
        else:
            oriMap[y, 2*x] = val
            oriMap[y, 2*x + 1] = val

def add_to_queue(queue, x, y, oriMap, explored, leftList, rightList):
    if x < 0 or x >= oriMap.shape[1] or y < 0 or y >= oriMap.shape[0]:
        return
    if explored[y, x]:
        return
    
    queue.put((x, y))
    explored[y, x] = True
    if oriMap[y, x] == "[":
        leftList.append((x, y))
    else:
        rightList.append((x, y))

def check_movable(orimap, nextX, nextY, direction):
    leftList, rightList = [], []
    toSearch = Queue()
    explored = np.zeros_like(oriMap, dtype=bool)
    add_to_queue(toSearch, nextX, nextY, oriMap, explored, leftList, rightList)
    while not toSearch.empty():
        searchX, searchY = toSearch.get()

        # check front
        frontX, frontY = searchX + direction[0], searchY + direction[1]
        if oriMap[frontY, frontX] == "#":
            return False, leftList, rightList
        if oriMap[frontY, frontX] == "[" or oriMap[frontY, frontX] == "]":
            add_to_queue(toSearch, frontX, frontY, oriMap, explored, leftList, rightList)
        
        # check the other half of the obstacle
        if oriMap[searchY, searchX] == "[":
            add_to_queue(toSearch, searchX+1, searchY, oriMap, explored, leftList, rightList)
        elif oriMap[searchY, searchX] == "]":
            add_to_queue(toSearch, searchX-1, searchY, oriMap, explored, leftList, rightList)
        else:
            print("something thas is not an obstacles is incorrectly added to the queue")

    return True, leftList, rightList

def move_obstacle(oriMap, leftList, rightList, direction):
    # clear the old position
    for x, y in leftList:
        oriMap[y, x] = "."
    for x, y in rightList:
        oriMap[y, x] = "."
    
    for x, y in leftList:
        oriMap[y+direction[1], x+direction[0]] = "["
    for x, y in rightList:
        oriMap[y+direction[1], x+direction[0]] = "]"

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
    
    if oriMap[testY, testX] == "." or oriMap[testY, testX] == "@": # empty spot
        oriMap[robY, robX] = "."
        oriMap[testY, testX] = "@"
        robX, robY = testX, testY
    elif oriMap[testY, testX] == "#": # immoveable wall
        pass # do nothing
    elif oriMap[testY, testX] == "[" or oriMap[testY, testX] == "]": # an obstacle
        ifMoveable, leftList, rightList = check_movable(oriMap, testX, testY, direction)
        if ifMoveable:
            move_obstacle(oriMap, leftList, rightList, direction)
            oriMap[robY, robX] = "."
            oriMap[testY, testX] = "@"
            robX, robY = testX, testY
        else:
            cxdaf = []

print(oriMap)
obstacles = np.where(oriMap == "[")
gps = np.sum(100 * obstacles[0] + obstacles[1])
print(f"gps: {gps}")
print("end")