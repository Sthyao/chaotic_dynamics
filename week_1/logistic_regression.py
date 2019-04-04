import numpy as np 
import matplotlib.pyplot as plt

"""Bifurcate and Chaos"""
"""Depending on x(n+1)=μx(n)-μx(n)^2 """

x = np.zeros(4000)
xn = np.zeros(4000)
r = np.linspace(0,4,4000,endpoint=True)
x = 0.5
"""Initial value"""

for i in range(0,150):
    x = np.multiply(np.multiply(r, x), 1-x)

for i in range(0,40):
    x = np.multiply( np.multiply(r, x), 1-x)
    plt.scatter(r,x,s = 0.01,c = 'k')

plt.show()

