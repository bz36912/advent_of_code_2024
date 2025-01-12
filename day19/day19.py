import numpy as np
from queue import Queue, LifoQueue

file = open("day19/Op.txt", "r")
text = file.read()
options = text.split(", ")
wOp = []
for op in options:
    if "w" == op[-1]:
        wOp.append(op)
def by_length(item):
    return len(item)
wOp.sort(key=by_length)
file = open("day19/input.txt", "r")
numPossible = 0

for i, line in enumerate(file):
    possible = False
    val = line.strip()
    toSearch = LifoQueue()
    toSearch.put(val)
    while not toSearch.empty():
        newVal = toSearch.get()
        if newVal == "" or newVal[-1] != "w":
            numPossible += 1
            possible = True
            print(f"line {i}: {val} is possible")
            break

        for op in wOp:
            if len(op) > len(newVal): # it is too long after adding the new towel
                continue
            if op == val[-len(op):]:
                toSearch.put(newVal[:-len(op)])
    
    if not possible:
        print(f"NOT possible at {i}: {val}")

print(f"numPossible = {numPossible}")
print("end")

# 285 is too high