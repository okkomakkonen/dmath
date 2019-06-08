from .dual import *
from .triple import *

def deriv(func):
    def derivative(x):
        return func(dual(x,1))[1]
    return derivative

def grad(func):
    def gradient(x,y):
        val = func(triple(x, 1, 0), triple(y, 0, 1))
        return (val[1], val[2])
    return gradient