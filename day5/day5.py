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
    intNums = []
    for num in nums:
        intNums.append(int(num))

    for intNum in intNums:
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
        sortedPages = []
        # order the pages
        while len(intNums) != 0:
            elem = intNums.pop(0)

            if elem not in rules_dict:
                sortedPages.append(elem)
                continue
            values = rules_dict[elem]

            violation_detected = False
            temp = sortedPages.copy()
            for page in temp:
                if page in values:
                    violation_detected = True
                    if violation_detected:
                        sortedPages.remove(page)
                        intNums.append(page)
            sortedPages.append(elem)
        
        increment = int(sortedPages[len(nums)//2])
        print(f"sorted: {sortedPages} contains {increment}")
        part2_total += increment
        # increment by the middle page number
print(f"total: {total}")
print(f"part2_total: {part2_total}")
print(f"end")