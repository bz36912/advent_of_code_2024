import numpy as np
file1 = open("day4/input.txt", "r")

total = 0
# search horizontally
horizontal = file1.read()
total += horizontal.count("XMAS")
total += horizontal.count("SAMX")

# search vertically
numCols = horizontal.index("\n")
numRows = numCols

vertical = ""
for row in range(numRows):
    for col in range(numCols):
        vertical += horizontal[col * (numCols + 1) + row]
    vertical += "\n"
print(f"vertical: {vertical}")
total += vertical.count("XMAS")
total += vertical.count("SAMX")

# search diagonally
diagonal1 = ""
for intecept in range(0, numCols * 2 - 1):
    for x in range(numCols):
        y = -x + intecept
        if y >= 0 and y < numRows:
            diagonal1 += horizontal[y * (numCols + 1) + x]
    diagonal1 += "\n"
print(f"diagonal1: {diagonal1}")
total += diagonal1.count("XMAS")
total += diagonal1.count("SAMX")

diagonal2 = ""
for intecept in range(-numCols + 1, numCols):
    for x in range(numCols):
        y = x + intecept
        if y >= 0 and y < numRows:
            diagonal2 += horizontal[y * (numCols + 1) + x]
    diagonal2 += "\n"
print(f"diagonal2: {diagonal2}")
total += diagonal2.count("XMAS")
total += diagonal2.count("SAMX")

print(total)
print("end")