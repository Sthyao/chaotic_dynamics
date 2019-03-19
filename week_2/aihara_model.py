import matplotlib.pyplot as plt 
import math
import numpy as np 

k = 0.5
b = 0.04
A = 1
x = 0
a = np.linspace(0,1,100000,endpoint=True)
y = np.zeros(100000)
leng = len(a)

for i in range(0,leng):
    y[i] = 0.5

for i in range(0,leng):
    y[i] = k * x - A * ( 1 / ( 1 + math.exp( -x / b ))) + a[i]
    x = y[i]

plt.scatter(a,y,s = 1,c = 'k')
plt.show()   
