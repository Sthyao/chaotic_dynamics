import matplotlib.pyplot as plt
import numpy as np
import math
import lab

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
        m = lab.ly(y)
        sm  = sm + math.log(m, 2)
        y = lab.f(y , a[i])
    ly[i] = sm / 2000

plt.scatter(a , ly ,s = 1, c = 'k')
plt.plot(linex,liney)
plt.show()