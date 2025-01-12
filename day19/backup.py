import numpy as np
from queue import Queue, LifoQueue

file = open("day19/Op.txt", "r")
text = file.read()
options = text.split(", ")
wOp = []
short = ['u', 'b', 'r', 'g', 'wu', 'ww', 'wb', 'wr', 'wg']
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
    toSearch.put([0, []])
    while not toSearch.empty():
        next_idx, history = toSearch.get()
        if next_idx >= len(val):
            possible = True
            numPossible += 1
            # print(f"line {i}: {val} is possible")
            break
        for op in short:
            if next_idx+len(op) > len(val): # it is too long after adding the new towel
                continue
            if op == val[next_idx:next_idx+len(op)]:
                newHist = history.copy()
                newHist.append((op))
                toSearch.put([next_idx+len(op), newHist])
    
    if not possible:
        print(f"NOT possible at {i}: {val}")
        if val[-1] != 'w':
            cdaf = []

print(f"numPossible = {numPossible}")
print("end")