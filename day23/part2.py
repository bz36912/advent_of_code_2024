import numpy as np
from collections import Counter
from queue import Queue, LifoQueue, PriorityQueue

def intersection(connections:dict, newNode:str, curSubSet:str, keys:list):
    intersected = Counter(connections[newNode])
    for node in curSubSet:
        intersected = intersected & Counter(connections[node])

    intersected = intersected & Counter(keys)
    # nodes, not in key, has already been explored, when root==intersect
    return list(intersected.elements())

def cal_priority(newCur:list, intersect:list):
    return 1024 - (len(newCur) + len(intersect) // 4)

connections = {}
file1 = open("day23/input.txt")
for i, line in enumerate(file1):
    nodes = line.strip().split("-")
    if nodes[0] not in connections:
        connections[nodes[0]] = []
    connections[nodes[0]].append(nodes[1])
    if nodes[1] not in connections:
        connections[nodes[1]] = []
    connections[nodes[1]].append(nodes[0])

keys = list(connections.keys()) # length of 520
largestSubset = ('oy', 'vb', 'sn', 'kp', 'wj', 'sz', 'kx', 'xh', 'dp', 'tq', 'yt', 'wm')
numSearches = 0
while len(keys) != 0:
    root = keys.pop()
    toSearch = PriorityQueue()
    priority = cal_priority((), ())
    toSearch.put((priority, (root, ())))

    while not toSearch.empty():
        ___, (newNode, curSet) = toSearch.get()
        numSearches += 1
        newCur = curSet + (newNode,)
        if len(newCur) > len(largestSubset):
            largestSubset = newCur

        intersects = intersection(connections, newNode, curSet, keys)
        if len(newCur) + len(intersects) <= len(largestSubset):
            continue
        priority = cal_priority(newCur, intersects)
        for intersect in intersects:
            toSearch.put((priority, (intersect, newCur)))

print(f"numSearch: {numSearches}")

print(len(largestSubset))
print(",".join(sorted(largestSubset)))
print("end")