""" The implementation is VERY sketchy since the AoC does not test many edge cases
1. Does not consider if Button A, B and Prize coordinates are co-linear / linearly dependent
2. Part B's + 10000000000000 means that significant figures are no where close to the decimal
    point, so the error tolerated by if_integer() is unrigorously large
"""
import numpy as np

def if_integer(x:np.double):
    return abs(x - round(x)) < 0.001

# parse the text file
file = open("day13/dummy.txt", "r")
text = file.read().strip()
machines = text.split("\n\n")
infos = []
for machine in machines:
    info = {}
    lines = machine.split("\n")
    plus = lines[0].split("+")
    Ay = int(plus[2])
    Ax = int(plus[1].split(",")[0])
    info["A"] = (Ax, Ay)

    plus = lines[1].split("+")
    Ay = int(plus[2])
    Ax = int(plus[1].split(",")[0])
    info["B"] = (Ax, Ay)

    equal = lines[2].split("=")
    Ay = int(equal[2])
    Ax = int(equal[1].split(",")[0])
    info["target"] = (Ax + 10000000000000, Ay + 10000000000000)
    infos.append(info)

tokens = 0
for i, info in enumerate(infos):
    a = np.array([[info["A"][0], info["B"][0]],
                  [info["A"][1], info["B"][1]]])
    b = np.array([[info["target"][0]], [info["target"][1]]])
    try:
        x = np.linalg.solve(a, b)
        if if_integer(x[0][0]) and if_integer(x[1][0]) and x[0] >= 0 and x[1] >= 0:
            tokens += x[0]*3 + x[1]
            print(f"{i, x}, succeeds")
        else:
            print(f"{i, x}, fails")
    except:
        print(f"{info} is not singular")        

print(f"token: {int(tokens)}")
print("end")