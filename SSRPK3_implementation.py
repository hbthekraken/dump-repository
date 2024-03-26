from decimal import Decimal, getcontext
from math import pi
import numpy as np
from matplotlib import pyplot as plt
# mp is for the specific example below
import mpmath as mp


plt.style.use("ggplot")
# some constants that can be used readily in the calculations
D = Decimal
getcontext().prec = 30
mp.mp.dps = 35
E, PI = D(1).exp(), D(f'{pi:.50f}')


# Example f: Approximation of Li(x) from 2 to x by ODE with SSPRK3
def f(t, y):
    return 1/+D(mp.ln(t).__str__())


# returns the data points at each t_n ((t_n, y_n)) as a list, where t_n is ranging from t0 to t_f
# Decimal class is used to reduce the loss of significance by arithmetic operations as much as possible
def SSPRK3(func, h, t0, y0at0, t_f):
    b1 = b2 = 1/D(6)
    b3 = 4*b1
    # c1 = D()
    # c2, c3 = D(1), D("0.5000")
    # a = [[0,0,0],[D(1),0,0],[1/D(4), 1/D(4), 0]]
    t = t0 if isinstance(t0, Decimal) else D(str(t0))
    yn = y0at0
    vals = [(t, y0at0)]
    kn = [D('NaN'), 0, 0 ,0]
    while t < t_f:
        kn[1] = func(t, yn)
        kn[2] = (func(t + h, yn + h*kn[1]))
        kn[3] = (func(t + h/2, yn + h*(kn[1]/4 + kn[2]/4)))
        yn1 = yn + h*(b1*kn[1] + b2*kn[2] + b3*kn[3])
        t += h
        vals.append((t, yn1,))
        yn = yn1
        
    print("DONE!")
    return vals


# The use of example function f (right hand side of the ODE, y' = f(t, y)) above is below
if __name__ == "__main__":
    points = SSPRK3(f, h=D("0.001"), t0=D(2), y0at0=D(0), t_f=D(20))
    x = np.array([p[0] for p in points])
    y = np.array([p[1] for p in points])
    print(points[-1])
    plt.plot(x, y, label="$y=Li_{2}(x): [2, 20) \\rightarrow [0, \infty)$")
    plt.legend()
    plt.show()
