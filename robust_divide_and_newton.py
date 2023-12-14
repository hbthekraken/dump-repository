import numpy as np

# divides the given 'domain' interval to n pieces, then looks for roots with Newton's method, assuming f is continuous on the given domain, 
# which ensures the proximity of the initial guess of the root to the actual root
def find_root(f, der_f, error_tol, n=1000, domain=(-10000, 10000)):    
    x = np.linspace(domain[0], domain[1], num=n)
    
    y = np.array(list(map(f, x)))
    I_0 = 0
    for i in range(1, len(x)):
        if y[i]*y[i - 1] < 0:
            I_0 = (x[i - 1], x[i],)
            break
        else:
            continue
    if not I_0:
        raise RuntimeError("No applicable roots found in the intervals, check your function, try higher values of n and/or different domains.")
    w = I_0[1] - I_0[0]
    I = [I_0]
    e1 = w
    i = 0
    while e1 > 0.01*w:
        I_next = (I[-1][0], (I[-1][0] + I[-1][1])/2, I[-1][1],)
        y_next = list(map(f, I_next))    
        
        if i > 10*n:
            break
        
        i += 1
        if y_next[0]*y_next[1] < 0:
            I.append((I_next[0], I_next[1],))
        else:
            I.append((I_next[1], I_next[2],))
    xo = (I[-1][0] + I[-1][1])/2
    x_n = xo
    i = -1
    if der_f:
        while True:
            diff = f(x_n)/der_f(x_n)
            x_n = x_n - diff
            i += 1
            if diff < 0.01*error_tol or i > n*10:
                return x_n
    else:
        h = 0.1*error_tol
        while True:
            slope = 0.5*(f(x_n + h) - f(x_n - h))/h
            diff = f(x_n)/slope
            x_n = x_n - diff
            i += 1
            if diff < 0.01*error_tol or i > n*10:
                return x_n

# below there is an example function applied to the function above
def g(x):   return x*x + np.exp(x*x) - 7


if __name__ == "__main__":
    a = find_root(g, 0, 1e-10, n=100, domain=(1, 2))
    print(a)
    
