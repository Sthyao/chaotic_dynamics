import numpy as np
import lab

a0 = 2
ar = 10
kf = 0.15
kr = 0.9


t = 1100
pattern = 0
M = 80

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

"""
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


"""
for i in range(4):
        lab.number_to_image(x[0][i],1000+i)

for i in range(4):
        sum = 0
        for j in range(100):
                sum += x[0][i][j]
        print(sum)

print(x[0][0])           