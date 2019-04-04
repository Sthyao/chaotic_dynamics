import numpy as np
import lab

a0 = 2
ar = 10
kf = 0.15
kr = 0.9
t = 200

a = np.array((
        1,1,0,0,0,0,0,0,1,1,
        1,1,1,0,0,0,0,1,1,1,
        0,1,1,1,0,0,1,1,1,0,
        0,0,1,1,1,1,1,1,0,0,
        0,0,0,1,1,1,0,0,0,0,
        0,0,0,0,1,1,1,0,0,0,
        0,0,1,1,1,1,1,1,0,0,
        0,1,1,1,0,0,1,1,1,0,
        1,1,1,0,0,0,0,1,1,1,
        1,1,0,0,0,0,0,0,1,1
))

b = np.array((
    0,0,0,0,0,1,0,0,0,0,
    0,0,0,0,1,1,1,0,0,0,
    0,0,0,0,1,1,1,0,0,0,
    0,0,0,1,1,1,1,1,0,0,
    0,0,0,1,1,0,1,1,0,0,
    0,0,1,1,1,0,1,1,1,0,
    0,0,1,1,0,0,0,1,1,0,
    0,1,1,1,0,0,0,1,1,1,
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

x = np.zeros((5001,4,100))
ni = np.zeros((5001,4,100))
ci = np.zeros((5001,4,100))

x[0][0] = pettern0[0]
x[0][1] = pettern0[1]
x[0][2] = pettern0[2]
x[0][3] = pettern0[3]


wij = np.zeros((100,100)) 

for i in range(100):
        for j in range(100):
                for p in range(4):
                        wij[i][j] += (2*x[0][p][i]-1)*(2*x[0][p][j]-1)
                wij[i][j] = wij[i][j]/4

for t in range(t):
        for n in range(4):
                for i in range(100):
                        wij_some = 0
                        for j in range(100):
                                wij_some += wij[i][j]*x[t][n][j]
                        ni[t+1][n][i] = kf*ni[t][n][i] + wij_some
                        ci[t+1][n][i] = kr*ci[t][n][i] - ar*x[t][n][i] + a0
                        x[t+1][n][i] = lab.sigmoid(ni[t+1][n][i]+ci[t+1][n][i])     
        lab.number_to_image(x[t][0],t)

"""
lab.number_to_image(x[0][0],10001)
lab.number_to_image(x[0][1],10002)
lab.number_to_image(x[0][2],10003)
lab.number_to_image(x[0][3],10004)
"""