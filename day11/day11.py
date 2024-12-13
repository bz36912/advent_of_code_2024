from time import time
import math
from threading import Thread
BLOCK_SIZE = 1000
FINAL_STAGE = 30
BLINK_PER_GROUP = 15

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
            # newNumbers.append(int(s[:len(s)//2]))
            # newNumbers.append(int(s[len(s)//2:]))
        else:
            newNumbers.append(num*2024)
    return newNumbers.copy()


file = open("day11/input.txt", "r")
text = file.read().strip()
numbers = text.split(" ")
numbers = [int(n) for n in numbers]
output = [None] * len(numbers)
startTime = time() 

for blink in range(30):
    numbers = compute(numbers)

copied = numbers.copy()
numbers = []
for num in copied:
    numbers2 = [num,]
    for blink in range(10):
        numbers2 = compute(numbers2)
    # print(f"{num} after 5 step has {len(numbers2)} stones")
    numbers.extend(numbers2)
print(f"after {FINAL_STAGE} blinks: {len(numbers)}, time: {time() - startTime}")

print("end")  