import numpy as np

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def update_count(value, m, s):
    if value == "M":
        return m + 1, s
    if value == "S":
        return m, s + 1
    return m, s

file1 = open("day4/input.txt", "r")

total = 0
# search horizontally
horizontal = file1.read()
numCols = horizontal.index("\n")
numRows = numCols

indice = find(horizontal, 'A')
for index in indice:
    # elimate letter A at the edge of the grid
    if index < numCols or index >= len(horizontal) - numCols:
        continue # since the A is in the first or last row
    if index % (numCols + 1) == 0 or index % (numCols + 1) == numCols - 1:
        continue # A is in the first or last column

    m, s = 0, 0
    m, s = update_count(horizontal[index - numCols - 2], m, s) # top left corner
    m, s = update_count(horizontal[index + numCols + 2], m, s) # bottom right

    if m == 1 and s == 1:
        pass
    else:
        continue
    
    m, s = 0, 0
    m, s = update_count(horizontal[index - numCols], m, s) # top right
    m, s = update_count(horizontal[index + numCols], m, s) # bottom left
    
    if m == 1 and s == 1:
        total += 1
        print(f"A at ({index // (numCols + 1)}, {index% (numCols + 1)})")

print(total)
print("end")