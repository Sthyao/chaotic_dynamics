import numpy as np
from PIL import Image
import lab

a0 = 2
ar = 0.7
kf = 0
kr = 0

a = np.array((
        1,1,0,0,0,0,0,0,1,1,
        0,1,1,0,0,0,0,1,1,0,
        0,0,1,1,0,0,1,1,0,0,
        0,0,0,1,1,1,1,0,0,0,
        0,0,0,0,1,1,0,0,0,0,
        0,0,0,1,1,1,1,0,0,0,
        0,0,1,1,0,0,1,1,0,0,
        0,1,1,0,0,0,0,1,1,0,
        1,1,0,0,0,0,0,0,1,1,
        0,0,0,0,1,0,0,0,0,0)
)

b = np.array((
    0,0,0,0,0,1,0,0,0,0,
    0,0,0,0,1,1,1,0,0,0,
    0,0,0,0,1,1,1,0,0,0,
    0,0,0,1,1,1,1,1,0,0,
    0,0,0,1,1,0,1,1,0,0,
    0,0,1,1,1,1,0,1,1,0,
    0,0,1,1,0,0,0,1,1,0,
    0,1,1,1,0,0,0,1,1,0,
    0,1,1,1,1,1,1,1,1,1,
    0,1,1,1,1,1,1,1,1,1,
))

c = np.array((
    0,0,1,1,1,0,0,0,1,1,
    0,1,1,1,1,1,1,1,1,1,
    1,1,1,0,1,1,1,1,0,0,
    1,1,0,0,0,1,1,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,1,1,0,0,0,1,1,
    0,0,1,1,1,1,0,1,1,1,
    1,1,1,1,1,1,1,1,1,0,
    1,1,0,0,0,1,1,1,0,0,
    0,0,0,0,0,0,0,0,0,0
))

d = np.array((
    0,0,1,0,0,0,0,1,0,0,
    0,0,1,1,0,0,1,1,0,0,
    0,0,1,1,1,1,1,1,0,0,
    0,0,1,1,1,1,1,1,0,0,
    0,0,1,1,1,1,1,1,0,0,
    0,1,1,1,1,1,1,1,1,0,
    1,1,1,1,1,1,1,1,1,1,
    0,0,0,1,1,1,1,0,0,0,
    0,0,0,0,1,1,0,0,0,0,
    0,0,0,0,0,1,0,0,0,0
))

pettern0 = [a,b,c,d]

def number_to_image(a):
        img = Image.new("RGB",(100,100))
        pixTupleB = (0,0,0,15)
        pixTupleW = (255,255,255,15)
        if a[0] >= 0.5:
                sum_ = np.ones((10,10))
        else:
                sum_ = np.zeros((10,10))
        for j in range(1,10):
                if a[j] >= 0.5 :
                        temp = np.ones((10,10))
                else:
                        temp = np.zeros((10,10))
                sum_ = np.hstack((sum_,temp))
        sum_0 = sum_
        for i in range(1,10):
                if a[i*10] >= 0.5:
                                sum_ = np.ones((10,10))
                else:
                        sum_ = np.zeros((10,10))
                for j in range(1,10):
                        if a[i*10+j] >= 0.5:
                                temp = np.ones((10,10))
                        else:
                                temp = np.zeros((10,10))
                        sum_ = np.hstack((sum_,temp))
                sum_0 = np.vstack((sum_0,sum_))
        for i in range(100):
                for j in range(100):
                        if sum_0[j][i] == 1:
                                img.putpixel((i,j),pixTupleB)
                        else:
                                img.putpixel((i,j),pixTupleW)
        img.show()


"""
def fw(pettern,i,j):
    wij = 0
    for k in range(4):
        wij += (pettern[k][i]-0.5)*(pettern[k][j]-0.5)
    return wij

def fn(pettern,x,i):
    w_sum = 0
    for j in range(100):
        w_sum += fw(pettern,i,j)*x[j]
    return w_sum + 0

def fc(x,a):
    return 0 - ar*x + a

def y(pettern,x,i,a):
    return fn(pettern,x,i) + fc(x,a)
"""

x = np.zeros((20,4,100))
x[0][0] = pettern0[0]
x[0][1] = pettern0[1]
x[0][2] = pettern0[2]
x[0][3] = pettern0[3]

for n in range(4):
    for i in range(100):
        wij = 0
        for k in range(100):
            for j in range(4):
                wij += (x[0][j][i]-0.5)*(x[0][j][k]-0.5)*x[0][j][k]
        x[1][n][i] = lab.f(a0 - 8* x[0][n][i] + wij,a0)


number_to_image(x[1][1])
print(x[1][0])

    
    
    
    




  

