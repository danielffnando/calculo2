import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

xcord = []
ycord = []
area = []
time = []

for i in np.linspace(0, 20, 51):
    x = i
    y = -x/2 + 10
    xcord.append(x)
    ycord.append(y)
    area.append(x*y)
    time.append(i)

mpl.rc('lines', linewidth=4, color='r')

#plt.figure(num=1, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
#plt.subplot(2, 1, 1)
plt.plot(xcord, ycord)
plt.title('Terreno')
plt.grid(True)

#plt.subplot(2, 1, 2)
#plt.plot(time, area)
#plt.title('Area')
#plt.xlabel('Time')
#plt.ylabel('Area')
#plt.grid(True)

plt.tight_layout()
plt.show()
