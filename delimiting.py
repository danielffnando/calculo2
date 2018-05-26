import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = np.arange(0.0, 20.0, 0.01)
#y = -x/2 + 10

y = -x/2 + 10

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure() and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='x', ylabel='y',
       title='y = -x/2 + 10')
ax.grid()

fig.savefig("test.png")
plt.show()
