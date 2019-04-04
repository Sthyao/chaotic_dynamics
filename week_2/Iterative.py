import matplotlib.pyplot as plt 
import numpy as np 
import math
import lab


a = 0.67 #0.77 / 0.70 / 0.67 / 0.55

yy = np.zeros((3,3))
yy1 = np.zeros(3)
yy2 = np.zeros(3)
yy0 = 0.01
xx0 = np.linspace(-1,1,200,endpoint=True)

leng = len(xx0)
y1 = np.zeros(leng)
y2 = np.zeros(leng)

for i in range(0,leng):
    y1[i] = lab.f(xx0[i], a)
    y2[i] = xx0[i]



for i in range(0,100):
    yy[0][0] = yy0
    yy[0][1] = lab.f(yy[0][0],a)
    yy[1][0] = yy[0][1]
    yy[1][1] = yy[0][1]
    yy[2][0] = yy[0][1]
    yy[2][1] = lab.f(yy[0][1],a)
    yy0 = yy[2][0]
    for j in range(0,3):
        yy1[j] = yy[j][0]
        yy2[j] = yy[j][1]
    plt.plot(yy1,yy2,c = 'k')

plt.plot(xx0,y1, c = 'k')
plt.plot(xx0,y2, c = 'k')
plt.show()