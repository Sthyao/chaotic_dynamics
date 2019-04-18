import numpy as np
import lab

a0 = 2
ar = 10
kf = 0.15
kr = 0.9

t = 1000
pattern = 0
M = 80

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
    0,0,1,1,0,0,1,1,0,0,
    0,0,1,1,0,0,1,1,0,0,
    0,0,1,1,1,1,1,1,0,0,
    0,0,1,1,1,1,1,1,0,0,
    0,0,1,1,1,1,1,1,1,0,
    0,1,1,1,1,1,1,1,1,0,
    1,1,1,1,1,1,1,1,1,1,
    0,0,0,1,1,1,1,0,0,0,
    0,0,0,0,1,1,0,0,0,0,
    0,0,0,0,0,1,0,0,0,0
))

pettern0 = [a,b,c,d]

x = np.zeros((5001,4,100))
ni = np.random.uniform(0, 1, (5001,4,100))
ci = np.random.uniform(0, 1, (5001,4,100))

x[0][0] = pettern0[0]
x[0][1] = pettern0[1]
x[0][2] = pettern0[2]
x[0][3] = pettern0[3]

process_bar = lab.ShowProcess(t,"ok")
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
                        max_ci = 0

                        for s in range(100):
                                max_ci += abs(ni[t][n][s])

                        for j in range(100):
                                wij_some += wij[i][j]*x[t][n][j]
                        max_ci = max_ci/M
                        ni[t+1][n][i] = kf*ni[t][n][i] + wij_some
                        ci[t+1][n][i] = kr*ci[t][n][i] - ar*x[t][n][i] + a0
            
                        if ci[t+1][n][i] >= max_ci and t != 0:
                            ci[t+1][n][i] = max_ci
                        elif ci[t+1][n][i] <= -max_ci and t != 0:
                            ci[t+1][n][i] = -max_ci

                        x[t+1][n][i] = lab.sigmoid(ni[t+1][n][i]+ci[t+1][n][i])     
        lab.number_to_image(x[t][pattern],t)
        process_bar.show_process()  

