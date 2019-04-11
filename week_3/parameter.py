import numpy as np
import lab
import matplotlib.pyplot as plt

a0 = 2
ar = 10
kf = 0.20
kr = 0.95

K = 0.6
belt = 0.945
es = 0

partten = 0
t = 400

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

process_bar = lab.ShowProcess(t,"ok")

for i in range(100):
        for j in range(100):
                for p in range(4):
                        wij[i][j] += (2*x[0][p][i]-1)*(2*x[0][p][j]-1)
                wij[i][j] = wij[i][j]/4

for t in range(t):
        for n in range(4):
                for i in range(100):
                        wij_some = 0
                        u_sum = 0.5
                        """
                        for s in range(100):
                                if t != 0:
                                        u_sum += abs(x[t][partten][s]-es)
                        """
                        for j in range(100):
                                wij_some += wij[i][j]*x[t][n][j]
                        ni[t+1][n][i] = kf*ni[t][n][i] + wij_some
                        ci[t+1][n][i] = kr*ci[t][n][i] - ar*(belt**(K*u_sum))*x[t][n][i] + a0
                        x[t+1][n][i] = lab.sigmoid(ni[t+1][n][i]+ci[t+1][n][i])   
        process_bar.show_process()  
        lab.number_to_image(x[t][partten],t)
        #plt.scatter(t,u_sum,s = 0.1, c = 'b')

#plt.show()

"""
lab.number_to_image(x[0][0],1)
lab.number_to_image(x[0][1],2)
lab.number_to_image(x[0][2],3)
lab.number_to_image(x[0][3],4)
"""

"""
if we change from u_sum += abs(x[t][partten][s]-x[t-1][partten][s]) 
to  u_sum += abs(x[t][partten][s]-x[t-1][partten][s]/2)

it's obvious that we get a higher quality of control
"""
