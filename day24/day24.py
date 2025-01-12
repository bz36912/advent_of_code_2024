import numpy as np

# indice
IN1, IN2, OP, OUT = 0, 1, 2, 3
knownWires = {}
dependencies = {}
init = open("day24/init.txt")
for i, line in enumerate(init):
    val = line.strip().split(": ")
    knownWires[val[0]] = int(val[1])
    dependencies[val[0]] = ()

connections = []
gates = open("day24/input.txt")
for i, line in enumerate(gates):
    val = line.strip().split(" ")
    connections.append((val[0], val[2], val[1], val[4]))

while len(connections) != 0:
    for i, c in enumerate(reversed(connections)):
        if c[IN1] in knownWires and c[IN2] in knownWires:
            if c[OP] == "AND":
                knownWires[c[OUT]] = knownWires[c[IN1]] & knownWires[c[IN2]]
            elif c[OP] == "OR":
                knownWires[c[OUT]] = knownWires[c[IN1]] | knownWires[c[IN2]]
            elif c[OP] == "XOR":
                knownWires[c[OUT]] = knownWires[c[IN1]] ^ knownWires[c[IN2]]
            else:
                assert(False)
            dependencies[c[OUT]] = dependencies[c[IN1]] + dependencies[c[IN2]] + (c[IN1], c[IN2])
            dependencies[c[OUT]] = tuple(set(dependencies))
            connections.remove(c)

def binary_string(letter:str):
    global knownWires
    binaryString = ""
    for i in range(100):
        key = letter + str(i).zfill(2)
        if key not in knownWires:
            break
        binaryString = str(knownWires[key]) + binaryString
    return binaryString

zString = binary_string("z")
x, y = int(binary_string("x"), 2), int(binary_string("y"), 2)
print(f"z in decimal: {int(zString, 2)}, but should be {x + y}")
print("comparison")

theoretical = bin(x+y)[2:]
print(f"a: {zString}")
print(f"t: {theoretical}")

differences = []
for i in range(len(theoretical)):
    if zString[i] != theoretical[i]:
        differences.append(i)
print(f"different indices: {differences}")
print("end")

# switches at indice: 9, 17, 28, 32
# a: 1100000111000000011010001000011110001011001110
# t: 1100000110111111111010001000100010001011001110