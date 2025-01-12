from time import time
import math
import numpy as np

BLINKS_PER_GROUP = 5
assert(75 % BLINKS_PER_GROUP == 0)

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

def group_blink_times(num:int):
    global lookup, repeat
    if num in lookup:
        numbers = lookup[num]
        repeat += 1
    else:
        numbers = [num,]
        for blink in range(BLINKS_PER_GROUP):
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

for i in range(75 // BLINKS_PER_GROUP):
    count = {}
    for j, num in enumerate(prevCount.keys()):
        outputs = group_blink_times(num)
        for out in outputs:
            if out not in count:
                count[out] = 0
            count[out] += prevCount[num]
    total = np.array(list(count.values())).sum()
    print(f"after {BLINKS_PER_GROUP*(i+1)} blinks: {total}, time: {time() - startTime}")
    prevCount = count

assert(total == 266820198587914)
print("end")  

# 3 X 25 blinks
# 50 blinks: 7725862493 after 140 sec
# 75 blinks: 266820198587914 after 1201 sec

# 5 X 15 blinks
# after 75 blinks: 266820198587914, time: 33.266
# len(lookup) = 3474, repeat = 2753

# 15 X 5 blinks
# after 75 blinks: 266820198587914, time: 2.338
# len(lookup) = 3753, repeat = 18779

# 25 X 3 blinks
# after 75 blinks: 266820198587914, time: 2.1242189407348633
# len(lookup) = 3811, repeat = 34895