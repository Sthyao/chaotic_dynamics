import matplotlib.pyplot as plt
import numpy as np
import math


k = 0.5 
b = 0.04
A = 1
a = np.linspace(0,4,10000,endpoint= True)
leng = len(a)
ly = np.zeros(10000)
liney = np .zeros(4100)
linex = np.arange(0.000,4.100,0.001)

def f(x,a):
    return  a * x* (1-x)

def lya(x):
    return abs( k + A * math.exp( -1 * x / b) / ( b * ( 1 + math.exp( -1 * x / b ))**2))

for i in range(0,leng):
    y = 0.5
    sm = 0
    m = 0.001
    for j in range(0, 2000):
        m = lya(y)
        sm  = sm + math.log(m, 2)
        y = f(y,a[i])
    ly[i] = sm / 2000

plt.plot(a , ly , c = 'k')
plt.plot(linex,liney)
plt.show()