import math
file = open("day9/input.txt", "r")

fileVal = []
emptySpots = []
for i in range(10):
    emptySpots.append([])

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
            fileVal.append((fileId, digit))
            fileId += 1
        else:
            emptySpots[digit].append(fileId)
            emptySpots[digit].sort()

print(emptySpots)

emptySpotsIdx = []
for i in range(fileId):
    emptySpotsIdx.append([])

idx = len(fileVal) - 1
for fid, size in reversed(fileVal.copy()):
    whichCapacity = None
    minIndex = math.inf
    for capacity in range(size, 10):
        if len(emptySpots[capacity]) == 0:
            continue
        firstIdx = emptySpots[capacity][0]
        if firstIdx < minIndex:
            minIndex = firstIdx
            whichCapacity = capacity
    
    if whichCapacity is None:
        idx -= 1
        continue
    
    emptyIdx = emptySpots[whichCapacity].pop(0)
    if emptyIdx <= idx:
        emptySpotsIdx[emptyIdx].append((fid, size))
        fileVal[idx] = (-1, size)
        spare = whichCapacity - size
        if spare > 0:
            emptySpots[spare].append(emptyIdx)
            emptySpots[spare].sort()
    idx -= 1

for capacity in range(1, 10):
    for spots in emptySpots[capacity]:
        emptySpotsIdx[spots].append((-1, capacity))

print(f"empty: {emptySpotsIdx}")
print(f"file: {fileVal}")

# calculate checksum
total = 0
pos = 0
for i in range(fileId):
    for e in emptySpotsIdx[i]:
        for j in range(e[1]):
            if e[0] != -1:
                total += pos * e[0]
            pos += 1

    for j in range(fileVal[i][1]):
        if fileVal[i][0] != -1:
            total += pos * fileVal[i][0]
        else:
            ck = 0
        pos += 1

print(f"total: {total}")
# 14146802128183 is too high for total
# 6346675637052 is too low
print("end")