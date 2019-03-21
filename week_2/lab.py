import math

k = 0.5
b = 0.02
A = 1
#init

def f(x,a):
    if (-x/b) >=25:
        return k * x - A * ( 1 / ( 1 + math.exp(25))) + a
    else:
        return k * x - A * ( 1 / ( 1 + math.exp( -1 * x / b))) + a

def ly(x):
    return abs( k + A * math.exp( -1 * x / b) / ( b * ( 1 + math.exp( -1 * x / b ))**2))