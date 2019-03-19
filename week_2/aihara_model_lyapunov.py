import matplotlib.pyplot as plt
import numpy as np
import math

k = 0.5 
b = 0.04
A = 1
a = np.linspace(0,1,10000,endpoint= True)
leng = len(a)
ly = np.zeros(10000)
liney = np .zeros(1100)
linex = np.arange(0.000,1.100,0.001)

for i in range(0,leng):
    y = 0.5
    sm = 0
    m = 0.001
    for j in range(0, 2000):
        m = abs( k + A * math.exp( - y / b) / ( b * ( 1 + math.exp( -y / b ))**2))
        sm  = sm + math.log(m, 2)
        y = k * y - A * ( 1 / ( 1 + math.exp( -y/b ) )) + a[i]
    ly[i] = sm / 2000

plt.scatter(a , ly ,s = 1, c = 'k')
plt.plot(linex,liney)
plt.show()