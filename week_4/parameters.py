import numpy as np
import lab

a0 = 2
ar = 10
kf = 0.15
kr = 0.9

t = 200
K = 0.6
belt = 0.945
es = 0.5
partten = 0

data = np.load('data.npz')
pettern0 = [data['a'],data['b'],data['c'],data['d']]
wij = data['wij']
process_bar = lab.ShowProcess(t,"ok")

x = np.zeros((5001,4,100))
ni = np.zeros((5001,4,100))
ci = np.zeros((5001,4,100))

x[0][0] = data['init']
x[0][1] = pettern0[1]
x[0][2] = pettern0[2]
x[0][3] = pettern0[3]

for t in range(t):
        for n in range(4):
                for i in range(100):
                        wij_some = 0
                        u_sum = 0.5
                        
                        for s in range(100):
                                if t != 0:
                                        u_sum += abs(x[t][partten][s]-es*x[t-1][partten][s])
                        
                        for j in range(100):
                                wij_some += wij[i][j]*x[t][n][j]
                        ni[t+1][n][i] = kf*ni[t][n][i] + wij_some
                        ci[t+1][n][i] = kr*ci[t][n][i] - ar*(belt**(K*u_sum))*x[t][n][i] + a0
                        x[t+1][n][i] = lab.sigmoid(ni[t+1][n][i]+ci[t+1][n][i]) 
        lab.number_to_image(x[t][0],t)  
        process_bar.show_process() 
