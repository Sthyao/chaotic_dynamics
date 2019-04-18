import numpy as np
import lab
import math

a0 = 2
ar = 10
kf = 0.15
kr = 0.9
t = 200

A = 7
A_ = 11
D = 13
b0 = 0
sert = 0


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


x = np.zeros((5001,4,100))
ni = np.zeros((5001,4,100))
ci = np.zeros((5001,4,100))

x[0][0] = pettern0[0]
x[0][1] = pettern0[1]
x[0][2] = pettern0[2]
x[0][3] = pettern0[3]


wij = np.zeros((100,100)) 
ni_max = 0
ci_max = 0

for i in range(100):
        for j in range(100):
                for p in range(4):
                        wij[i][j] += (2*x[0][p][i]-1)*(2*x[0][p][j]-1)
                wij[i][j] = wij[i][j]/4
process_bar = lab.ShowProcess(t,"ok")

for t in range(t):
        for n in range(4):
                for i in range(100):
                        wij_some = 0
                        for j in range(100):
                                wij_some += wij[i][j]*x[t][n][j]

                        ni[t+1][n][i] = kf*ni[t][n][i] + wij_some
                        ci[t+1][n][i] = kr*ci[t][n][i] - ar*x[t][n][i] + a0

                        ni_max = A + D*math.sin(b0*t+sert)
                        ci_max = A_ + D*math.sin(b0*t+sert)
                        
                        if ni[t+1][n][i] >= ni_max :
                            ni[t+1][n][i] = ni_max
                        elif ni[t+1][n][i] <= -ni_max:
                            ni[t+1][n][i] = -ni_max
                        
                        if ci[t+1][n][i] >= ci_max:
                            ci[t+1][n][i] = ci_max
                        elif ci[t+1][n][i] <= -ci_max:
                            ci[t+1][n][i] = -ci_max

                        x[t+1][n][i] = lab.sigmoid(ni[t+1][n][i]+ci[t+1][n][i])     
        lab.number_to_image(x[t][0],t)
        process_bar.show_process()  

"""
lab.number_to_image(x[0][0],10001)
lab.number_to_image(x[0][1],10002)
lab.number_to_image(x[0][2],10003)
lab.number_to_image(x[0][3],10004)
"""