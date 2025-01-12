from collections import Counter
import math

connections = {}
file1 = open("day23/input.txt")
for i, line in enumerate(file1):
    nodes = line.strip().split("-")
    if nodes[0] not in connections:
        connections[nodes[0]] = [nodes[0],]
    connections[nodes[0]].append(nodes[1])
    if nodes[1] not in connections:
        connections[nodes[1]] = [nodes[1],]
    connections[nodes[1]].append(nodes[0])

keys = list(connections.keys())
NUM_GROUPS = 40
equalSize = len(keys) // NUM_GROUPS
groups = []
for i in range(NUM_GROUPS):
    group = keys[i*equalSize:(i+1)*equalSize].copy()
    groups.append(group)

for step in range(30):
    prevGroup = groups.copy()
    groupScores = [0] * NUM_GROUPS

    for i, g in enumerate(prevGroup):
        for e in g:
            bestGroup = -1
            bestScore = -math.inf
            for j, group in enumerate(prevGroup):
                intersected = Counter(connections[e]) & Counter(group)
                i_l = list(intersected.elements())
                score = 2 * len(i_l) - len(group)
                if score > bestScore:
                    bestScore = score
                    bestGroup = j
            groups[i].remove(e)
            groups[bestGroup].append(e)
            groupScores[bestGroup] += bestScore

longest_length = 0
longest_list = -1
for i, group in enumerate(groups):
    if len(group) > longest_length:
        longest_length = len(group)
        longest_list = i
print(f"groupScores: {groupScores}")
bestScoreGroupIdx = groupScores.index(max(groupScores))
print(",".join(sorted(groups[bestScoreGroupIdx])))
print("end")