import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
#from matplotlib.lines import Line2D as line

fig, ax1 = plt.subplots()
#ax2 = plt.subplots()
xp1, yp1, xarea, yarea = [], [], [], []
pt1, = plt.plot([], [], 'ro', animated=True)
pt2, = plt.plot([], [], 'ro', animated=True)
pt3, = plt.plot([], [], 'ro', animated=True)

ln1, = plt.plot([], [], '-b', animated=True)
ln2, = plt.plot([], [], '-b', animated=True)

xcord, ycord, area, time = [], [], [], []

for i in np.linspace(0, 20, 51):
    x = i
    y = -x/2 + 10
    xcord.append(x)
    ycord.append(y)
    area.append(x*y)
    time.append(i)

#plt.figure(num=1, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
#plt.subplot(2, 1, 1)
plt.plot(xcord, ycord)
plt.title('Terreno')
plt.grid(True)

def init():
    ax1.set_xlim(0, 22)
    ax1.set_ylim(0, 12)
#    ax2.set_xlim(0, 22)
#    ax2.set_ylim(0, 12)
    return pt1,
#    return ln2,

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
