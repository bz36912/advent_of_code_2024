# I think AoC's solution is not correct for Part 2. 
# 20 is the correct number of seconds.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

WIDTH,HEIGHT = 101, 103
file = open("day14/input.txt", "r")
text = file.read().strip()
robots = text.split("\n")
infos = []

ax:plt.Axes
fig, ax = plt.subplots()
ax.set_ylim(0, HEIGHT)
ax.set_xlim(0, WIDTH)
plt.ion()
scatter = Line2D([], [], linestyle='None', marker="o")
ax.add_line(scatter)

# tree at 20, 121, 222, 323
for step in range(6880, 6900):
    x, y = [], []
    quadrant = [[0, 0], [0,0]]
    # oriMap = np.zeros((HEIGHT, WIDTH), dtype=int)
    for robot in robots:
        info = {}
        parts = robot.split(" ")
        pStr = parts[0].split("=")[1]
        vStr = parts[1].split("=")[1]

        info["p"] = eval(f"({pStr})")
        info["v"] = eval(f"({vStr})")
        finalX = (info["p"][0] + info["v"][0] * step) % WIDTH
        finalY = (info["p"][1] + info["v"][1] * step) % HEIGHT
        x.append(finalX)
        y.append(finalY)
        # oriMap[finalY, finalX] += 1
        if finalX < WIDTH//2 and finalY < HEIGHT//2:
            quadrant[0][0] += 1
        elif finalX < WIDTH//2 and finalY > HEIGHT//2:
            quadrant[1][0] += 1
        elif finalX > WIDTH//2 and finalY < HEIGHT//2:
            quadrant[0][1] += 1
        elif finalX > WIDTH//2 and finalY > HEIGHT//2:
            quadrant[1][1] += 1
        infos.append(info)

    ax.set_title(f"step {step}")
    scatter.set_data(x, y)
    plt.pause(0.5)

# print(oriMap)
print(f"safety factor: {quadrant[0][0] * quadrant[0][1] * quadrant[1][0] * quadrant[1][1]}")
print("end")