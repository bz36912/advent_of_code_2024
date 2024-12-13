import numpy as np
file = open("day8/input.txt", "r")

text = file.read()
frequencies = list(set(text))
numCol = text.index("\n")

# create a map using a 2D numpy array
oriMap = np.zeros((numCol, numCol), dtype=str)
for x in range(numCol):
    for y in range(numCol):
        oriMap[y, x] = text[y * (numCol + 1) + x]

antinode = []
for freq in frequencies:
    if freq == "\n" or freq == "." or freq == "#":
        continue
    y, x = np.where(oriMap == freq)

    # find all pairs between antenna i and antenna j
    for i in range(x.size):
        antinode.append((x[i], y[i]))
        for j in range(x.size):
            if i == j:
                continue
            for k in range(numCol):
                aX = x[i] + k*(x[i] - x[j])
                aY = y[i] + k*(y[i] - y[j])
                if aX >= 0 and aY >= 0 and aX < numCol and aY < numCol:
                    antinode.append((aX, aY))
                    # if oriMap[aY, aX] != "#":
                    #     print(f"{(aY, aX)} is incorrect")
                else:
                    break

print(f"number of antinodes: {len(set(antinode))}")
print("end")