import numpy as np

connections = {}
file1 = open("day23/dummy.txt")
for i, line in enumerate(file1):
    nodes = line.strip().split("-")
    if nodes[0] not in connections:
        connections[nodes[0]] = []
    connections[nodes[0]].append(nodes[1])
    if nodes[1] not in connections:
        connections[nodes[1]] = []
    connections[nodes[1]].append(nodes[0])

clusters = set()
for key in connections.keys():
    if key[0] != 't':
        continue

    nodes = connections[key]
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[i] in connections[nodes[j]]:
                clusters.add(tuple(sorted((key, nodes[i], nodes[j]))))

print(f"num sets: {len(clusters)}")
print("end")