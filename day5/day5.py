import numpy as np
rules = open("day5/rules.txt", "r")

total = 0
part2_total = 0

rules_dict = {}
for line in rules:
    nums = line.split("|")
    key, val = int(nums[0]), int(nums[1])
    if key in rules_dict:
        rules_dict[key].append(val)
    else:
        rules_dict[key] = [val,]

order = open("day5/input.txt", "r")
for line in order:
    nums = line.split(",")
    seen = []
    correctOrder = True
    for num in nums:
        intNum = int(num)
        if intNum in seen:
            print(f"num {intNum} is repeated in {line}")
        seen.append(intNum)
        if intNum not in rules_dict:
            continue

        values = rules_dict[intNum]
        
        for value in values:
            if value in seen:
                correctOrder = False
                break

    if correctOrder:
        increment = int(nums[len(nums)//2])
        print(f"{line} contains {increment}")
        total += increment
    else:
        pass
        # order the pages
        
        # increment by the middle page number
print(f"total: {total}")