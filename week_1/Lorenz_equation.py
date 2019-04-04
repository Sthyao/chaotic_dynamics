from scipy.integrate import odeint 
import numpy as np 
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def lorenz(w,t,p,r,b):
    x , y, z = w
    return np.array([p*(y-x),x*(r-z)-y,x*y-b*z])

t = np.arange(0, 30, 0.01)

track1 = odeint(lorenz,
                (0.0,1.00,0.0),t, 
                args = (10.0,28.0,3.0))
track2 = odeint(lorenz,
                (0.0,1.05,0.0),t, 
                args = (10.0,28.0,3.0))

tr = track2-track1
fig = plt.figure()
ax = Axes3D(fig)


#ax.plot(tr[:,0],tr[:,1],tr[:,2], c = 'r')
#plt.show()


ax.plot(track1[:,0],track1[:,1],track1[:,2], c = 'k')
plt.show()

#ax.plot(track2[:,0],track2[:,1],track2[:,2], c = 'g')
#plt.show()


#if change the initial value
#track2 = odeint(lorenz,
#                (0.0,1.05,0.0),t, 
#                args = (10.0,28.0,3.0))
#tr = track2 - track1
#this pattern was showed by png2