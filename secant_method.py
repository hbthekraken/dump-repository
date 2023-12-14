from matplotlib import pyplot as plt
import numpy as np
import statistics as stat


plt.style.use("ggplot")

##H = np.linspace(1e-9, 1e-1, 10)
X = np.linspace(-10000, 10000, 10000)


def f(x):   return np.arctan(x)


if __name__ == "__main__":
  Y = 1/(1 + X*X)

  means1, means2, stdevs1, stdevs2 = [], [], [], []

  fig, ax = plt.subplots()

  N = np.array(list(range(0, 11)))

  for n in N:
    h = 10.0 ** (-n)
    
    sec1 = np.array([(f(x + h) - f(x))/h for x in X])
    sec_avg = np.array([(f(x + h) - f(x - h))/(2*h) for x in X])

    rel_err1 = 100*np.abs(Y - sec1)/Y
    rel_err2 = 100*np.abs(Y - sec_avg)/Y

    means1.append(stat.mean(rel_err1))
    means2.append(stat.mean(rel_err2))

    stdevs1.append(stat.stdev(rel_err1))
    stdevs2.append(stat.stdev(rel_err2))

  means1, means2, stdevs1, stdevs2 = np.array(means1), np.array(means2), np.array(stdevs1), np.array(stdevs2)

  ax.bar(N, means1 + stdevs1, bottom=(means1 - stdevs1), alpha=0.7, width=0.35)
  ax.bar(N, means2 + stdevs2, bottom=(means2 - stdevs2), alpha=0.7, width=0.35)
  
  ax.scatter(N, means1, label="Classical Secant Method MREs")
  ax.scatter(N, means2, label="Averaged Secant Method MREs")


  ax.axhline(linewidth=0.7, color="black")
  ax.axvline(linewidth=0.7, color="black")

  ax.legend()

  fig.tight_layout()
  plt.show()
  

##  print(f'For Classical Secant Method, h = {h}, Mean Relative Error is = {stat.mean(rel_err1)}\nStandard Deviation) = {stat.stdev(rel_err1)}')
##  print(f'For Averaged Secant Method, h = {h}, Mean Relative Error is = {stat.mean(rel_err2)}\nStandard Deviation) = {stat.stdev(rel_err2)}')
##  fig, ax = plt.subplots()
##
##  ax.plot(X, Y, label="Real Derivative", linewidth=4)
##  ax.plot(X, sec1, label=f'Clss. Sec. h = {h}')
##  ax.plot(X, sec_avg, label=f'Avg Sec. h = {h}')
##
##  ax.legend()
##  fig.tight_layout()
##  plt.show()
