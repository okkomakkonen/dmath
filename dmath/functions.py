import math
from .dual import dual

def exp(x):
    if isinstance(x, dual):
        val = math.exp(x[0])
        deriv = val
        return dual(val, *[deriv*a for a in x[1:]])
    else:
        return math.exp(x)

def sin(x):
    if isinstance(x, dual):
        val = math.sin(x[0])
        deriv = math.cos(x[0])
        return dual(val, *[deriv*a for a in x[1:]])
    else:
        return math.sin(x)

def cos(x):
    if isinstance(x, dual):
        val = math.cos(x[0])
        deriv = -math.sin(x[0])
        return dual(val, *[deriv*a for a in x[1:]])
    else:
        return math.cos(x)

def log(x):
    if isinstance(x, dual):
        val = math.log(x[0])
        deriv = 1/x[0]
        return dual(val, *[deriv*a for a in x[1:]])
    else:
        return math.log(x)

def sqrt(x):
    return x**0.5

def cbrt(x):
    return x**(1/3)

