import numpy as np
import lab
#import data

a0 = 2
ar = 10
kf = 0.15
kr = 0.9

t = 200

data = np.load('data.npz')
pettern0 = [data['a'],data['b'],data['c'],data['d']]
#pettern0 =  [data.a,data.b,data.c,data.d]

x = np.zeros((5001,4,100))
ni = np.zeros((5001,4,100))
ci = np.zeros((5001,4,100))

x[0][0] = pettern0[0]
x[0][1] = pettern0[1]
x[0][2] = pettern0[2]
x[0][3] = pettern0[3]



wij = data['wij']
#wij = np.zeros((100,100))
"""
for i in range(100):
        for j in range(100):
                for p in range(4):
                        wij[i][j] += (2*x[0][p][i]-1)*(2*x[0][p][j]-1)
                wij[i][j] = wij[i][j]/4

init = lab.random_init()

np.savez('data.npz',wij=wij,init=init,a=x[0][0],b=x[0][1],c=x[0][2],d=x[0][1])

"""
process_bar = lab.ShowProcess(t,"ok")
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
        process_bar.show_process()  

