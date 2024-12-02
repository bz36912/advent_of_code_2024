import numpy as np
file1 = open("day1/input.txt", "r")

leftList = []
rightList = []
for line in file1:
    line = line.strip()
    numbers = line.split(" ")
    leftList.append(int(numbers[0]))
    rightList.append(int(numbers[3]))

leftArr = np.sort(np.array(leftList))
rightArr = np.sort(np.array(rightList))

total = 0
for i in range(leftArr.size):
    val = leftArr[i]
    countInRight = np.sum(rightArr == val)
    total += countInRight * val
    # total += abs(leftArr[i] - rightArr[i])

print(total)
print("end")