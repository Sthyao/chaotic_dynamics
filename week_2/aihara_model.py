import matplotlib.pyplot as plt 
import math
import numpy as np 
import lab


x = 0
a = np.linspace(0,1,100000,endpoint=True)
y = np.zeros(100000)
leng = len(a)

for i in range(0,leng):
    y[i] = 0.5

for i in range(0,leng):
    y[i] = lab.f(x,a[i])
    x = y[i]

plt.scatter(a,y,s = 1,c = 'k')
plt.show()   
