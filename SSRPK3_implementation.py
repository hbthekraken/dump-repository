from decimal import Decimal, getcontext
from math import pi


D = Decimal
E, PI = D(1).exp(), D(f'{pi:.50f}')
k = D("0.0100000000")


def f(t, y):
    c = D("-0.0015")
    return k*(3*(c*t*t).exp() - 3 - y)



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

telemetry = SSPRK3(f, D("1E-4"), 30, 1200)

tel = open("C:/Users/Hüseyin Bıyıklı/Desktop/tele.txt", 'w')


for tpl in telemetry[::10000]:
    tel.write(str(tpl[0]).replace(".", ",") + " | " + str(tpl[1]).replace(".",",") + '\n')


tel.flush()
tel.close()
