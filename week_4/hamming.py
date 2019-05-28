import numpy as np 
import lab

data = np.load('data.npz')

print(lab.hamming(data['init'],data['a']))
print(lab.hamming(data['init'],data['b']))
print(lab.hamming(data['init'],data['c']))
print(lab.hamming(data['init'],data['d']))

#print(data['init'])