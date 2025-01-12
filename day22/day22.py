import numpy as np

BIT_MASK = 2**24-1

def next_number(num):
    num = (num ^ (num << 6)) & BIT_MASK
    num = (num ^ (num >> 5)) & BIT_MASK
    num = (num ^ (num << 11)) & BIT_MASK
    return num

def valid_sequence(seq:tuple):
    culminative = (seq[0], seq[0]+seq[1], seq[0]+seq[1]+seq[2], seq[0]+seq[1]+seq[2]+seq[3])
    return max(culminative) == culminative[-1] # ends on the highest price

total = 0
file = open("day22/input.txt")
allSeqToPrice = []
for line in file:
    val = line.strip()
    num = int(val)
    diffBuffer = (0, 0, 0, 0)
    seqToPrice = {}
    for i in range(2000):
        temp = next_number(num)
        ones = temp % 10
        diffBuffer = diffBuffer[1:] + (ones - num % 10,)
        if i >= 3 and valid_sequence(diffBuffer):
            if diffBuffer not in seqToPrice:
                seqToPrice[diffBuffer] = ones
        num = temp
    print(num)
    total += num
    allSeqToPrice.append(seqToPrice)

print(f"total: {total}")

allSeq = []
for seqToPrice in allSeqToPrice:
    seqToPrice:dict
    allSeq.extend(seqToPrice.keys())
allSeq = set(allSeq)

bestPrice = 0
for i, seq in enumerate(allSeq):
    totalPrice = 0
    for seqToPrice in allSeqToPrice:
        if seq not in seqToPrice:
            continue
        totalPrice += seqToPrice[seq]
    if totalPrice > bestPrice:
        bestPrice = totalPrice

print(f"bestSum: {bestPrice}")
print("end")

# 37327623
# Part 2 input.txt correct answer: 1898