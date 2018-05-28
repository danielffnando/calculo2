import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xsize, ysize, xarea, yarea = [], [], [], []
ln, = plt.plot([], [], 'ro', animated=True)
xcord, ycord, area, time = [], [], [], []

for i in np.linspace(0, 20, 51):
    x = i
    y = -x/2 + 10
    xcord.append(x)
    ycord.append(y)
    area.append(x*y)
    time.append(i)

plt.plot(time, area)
plt.title('Area')
plt.xlabel('Time')
plt.ylabel('Area')
plt.grid(True)

def init():
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 52)
    return ln,

def update(frame):
    xsize = frame
    ysize = frame * (-frame/2 + 10)
    ln.set_data(xsize, ysize)
    return ln,


ani = FuncAnimation(fig, update, frames=np.linspace(0, 20, 200),
                    init_func=init, blit=True)
plt.show()
#ani.save('Animation2.mp4')
