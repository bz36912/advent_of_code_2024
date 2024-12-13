import numpy as np
file = open("day9/dummy.txt", "r")

fileVal = []

fileId = 0
notEnd = True
while notEnd:
    for i in range(2):
        digit = file.read(1)
        if digit == '': 
            notEnd = False
            break
        else:
            digit = int(digit)
        
        if i == 0:
            fileVal.extend(digit * [str(fileId),])
            fileId += 1
        else:
            fileVal.extend(digit * [".",])
    
# print(f"fileVal: {fileVal}")
originalLength  = len(fileVal)

# compress fileVal
idx = len(fileVal) - 1
startSearchIdx = 0
for c in reversed(fileVal):
    if c == ".":
        idx -= 1
        continue
    emptyIdx = fileVal.index(".", startSearchIdx)
    startSearchIdx = emptyIdx
    if emptyIdx < idx:
        fileVal[emptyIdx] = c
        fileVal[idx] = "."
    else:
        break
    idx -= 1

# fileVal = "".join(fileVal) # convert back to string
# print(f"compressed: {fileVal}")

# checksum
total = 0
for i, c in enumerate(fileVal):
    if c == ".":
        continue
    total += i * int(c)
print(f"total: {total}")
print("end")