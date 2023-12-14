from decimal import Decimal, getcontext
from math import pi


D = Decimal
E, PI = D(1).exp(), D(f'{pi:.50f}')
k = D("0.0100000000")

# an example function f in the equation y' = f(t, y), here it is y' = k*(3*exp(c*t^2) - 3 - y)
def f(t, y):
    c = D("-0.0015")
    return k*(3*(c*t*t).exp() - 3 - y)


# returns the data points of y in the O.D.E. of the form y' = f(t, y) from 0 to t_f with initial value y(t_0) = y0_at0
def SSPRK3(func, h, y0at0, t_f):
    b1 = b2 = 1/D(6)
    b3 = 2*b2
    c1 = D()
    c2, c3 = D(1), D("0.5000")
    a = [[0,0,0],[D(1),0,0],[1/D(4), 1/D(4), 0]]
    t = D()
    yn = y0at0
    vals = [(0, y0at0)]
    while t <= t_f:
        kn = [D('NaN'), func(t, yn)]
        kn.append(func(t + h, yn + h*kn[1]))
        kn.append(func(t + h/2, yn + h*(kn[1]/4 + kn[2]/4)))
        yn1 = yn + h*(b1*kn[1] + b2*kn[2] + b3*kn[3])
        t += h
        vals.append((t, yn1,))
        yn = yn1
        if int(t*10000) % 10000 == 0:
            print("t is at {0} seconds, processing...".format(t))
    
    print("DONE!")
    return vals

if __name__ == '__main__':
    print(SSPRK3(f, D("0.01"), 0, 2))
