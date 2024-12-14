from time import time
import math
import numpy as np

lookup = {}
repeat = 0
def compute(numbers):
    newNumbers = []
    for num in numbers:
        # s = str(num)
        if num == 0:
            newNumbers.append(1)
            continue
        
        numDigits = int(math.log10(num)) + 1
        if numDigits % 2 == 0:
            factor = 10**(numDigits//2)
            newNumbers.append(num % factor)
            newNumbers.append(num // factor)
        else:
            newNumbers.append(num*2024)
    return newNumbers

def blink_15_times(num:int):
    global lookup, repeat
    if num in lookup:
        numbers = lookup[num]
    else:
        numbers = [num,]
        for blink in range(15):
            numbers = compute(numbers)
        lookup[num] = numbers.copy()
    return numbers

file = open("day11/input.txt", "r")
text = file.read().strip()
numbers = text.split(" ")
prevCount = {}
for n in numbers:
    intN = int(n)
    if intN not in numbers:
        prevCount[intN] = 0
    prevCount[intN] += 1

output = [None] * len(numbers)
startTime = time()

for i in range(5):
    count = {}
    for j, num in enumerate(prevCount.keys()):
        outputs = blink_15_times(num)
        for out in outputs:
            if out not in count:
                count[out] = 0
            count[out] += prevCount[num]
    total = np.array(list(count.values())).sum()
    print(f"after {15*(i+1)} blinks: {total}, time: {time() - startTime}")
    prevCount = count

print("end")  

# 50 blinks: 7725862493 after 140 sec
# 75 blinks: 266820198587914 after 1201 sec