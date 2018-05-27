import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax1 = plt.subplots()

xp1, yp1, xarea, yarea = [], [], [], []

### POINTS ###
pt1, = plt.plot([], [], 'ro', animated=True)
pt2, = plt.plot([], [], 'ro', animated=True)
pt3, = plt.plot([], [], 'ro', animated=True)

### LINES ###
ln1, = plt.plot([], [], '-b', animated=True)
ln2, = plt.plot([], [], '-b', animated=True)

### CREATING THE DIAGONAL LINE  F(X) = -X/2 + 10
xcord, ycord, area, time = [], [], [], []

for i in np.linspace(0, 20, 51):
    x = i
    y = -x/2 + 10
    xcord.append(x)
    ycord.append(y)
    area.append(x*y)
    time.append(i)

plt.plot(xcord, ycord)
plt.title('Terreno')
plt.grid(True)


### DEALING WITH THE ANIMATION ###
def init():
    ax1.set_xlim(0, 22)
    ax1.set_ylim(0, 12)
    return pt1,
def update(frame):
    xp1 = frame
    yp1 = -(frame)/2 + 10
    xp2 = frame
    yp2 = 0
    xp3 = 0
    yp3 = -(frame)/2 + 10
    pt1.set_data(xp1, yp1)
    pt2.set_data(xp2, yp2)
    pt3.set_data(xp3, yp3)

    ln1.set_data([yp1, xp1], [xp1, yp2])
    ln2.set_data([xp3, yp3], [yp1, xp1])
    return pt1, pt2, pt3, pt1, ln1, ln2,


ani = FuncAnimation(fig, update, frames=np.linspace(0, 20, 200),
                    init_func=init, blit=True)
plt.show()
