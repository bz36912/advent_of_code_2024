import numpy as np
file1 = open("day2/input.txt", "r")

numSafe = 0
for line in file1:
    line = line.strip()
    numbers = line.split(" ")
    ints = []
    for num in numbers:
        ints.append(int(num))

    for i in range(-1, len(ints)):
        if i == -1:
            arr = np.array(ints)
        else:
            temp = ints.copy()
            temp.pop(i)
            arr = np.array(temp)

        diff = arr[1:] - arr[:-1]

        numPositive = np.sum(diff > 0)
        numNegative = np.sum(diff < 0)

        if np.sum(diff == 0) != 0:
            continue

        if numPositive == 0:
            # all decreasing
            if np.min(diff) >= -3:
                numSafe += 1
                print(f"{line} is all decreasing")
                break

        if numNegative == 0:
            # all increasing
            if np.max(diff) <= 3:
                numSafe += 1
                print(f"{line} is all increasing")
                break

print(numSafe)
print("end")