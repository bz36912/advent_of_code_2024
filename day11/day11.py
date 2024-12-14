from time import time
import math
from threading import Thread
import numpy as np

FINAL_STAGE = 25

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
    return newNumbers.copy()

file = open("day11/input.txt", "r")
text = file.read().strip()
numbers = text.split(" ")
numbers = [int(n) for n in numbers]
output = [None] * len(numbers)
startTime = time() 

for blink in range(FINAL_STAGE):
    numbers = compute(numbers)

np.unique(np.numbers)

# def thread_entry(value:list, index:int):
#     numbers = value.copy()
#     for blink in range(FINAL_STAGE):
#         numbers = compute(numbers)
#     output[index] = numbers

# threads = []
# for i, num in enumerate(numbers):
#     threadName = Thread(target=thread_entry, args=([num,], i))
#     threadName.start()
#     threads.append(threadName)

# for thread in threads:
#     thread:Thread
#     thread.join()

# numbers = [i for row in output for i in row]

print(f"after {FINAL_STAGE} blinks: {len(numbers)}, time: {time() - startTime}")

print("end")  