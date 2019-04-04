import numpy as np 
import matplotlib.pyplot as plt 

x = np.zeros(100)
t = np.linspace(0,50,100,endpoint=True)

r = 3.3
x[0] = 0.1

for i in range(99):
    x[i+1] = r * x[i] * (1-x[i])

plt.plot(t,x,c = 'k')
plt.show()
