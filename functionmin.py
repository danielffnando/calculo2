import numpy as np
from scipy.optimize import fsolve

def func(X):
    x = X[0]
    y = X[1]
    L = X[2] # this is the multiplier. lambda is a reserved keyword in python
    return x*y + L * (x + 2*y - 20)
def dfunc(X):
    dLambda = np.zeros(len(X))
    h = 1e-3 # this is the step size used in the finite difference.
    for i in range(len(X)):
        dX = np.zeros(len(X))
        dX[i] = h
        dLambda[i] = (func(X+dX)-func(X-dX))/(2*h);
    return dLambda
# this is the max
X1 = fsolve(dfunc, [5, 10, 20])
print X1, func(X1)

# this is the min
X2 = fsolve(dfunc, [-1, -1, 0])
print X2, func(X2)
