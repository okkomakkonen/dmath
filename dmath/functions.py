import math
from .dual import *
from .triple import *

def exp(x):
    if isinstance(x, dual):
        val = math.exp(x[0])
        return dual(val, x[1]*val)
    elif isinstance(x, triple):
        val = math.exp(x[0])
        return triple(val, x[1]*val, x[2]*val)
    else:
        return math.exp(x)

def sin(x):
    if isinstance(x, dual):
        return dual(math.sin(x[0]), x[1]*math.cos(x[0]))
    elif isinstance(x, triple):
        return triple(math.sin(x[0]), x[1]*math.cos(x[0]), x[2]*math.cos(x[0]))
    else:
        return math.sin(x)

def cos(x):
    if isinstance(x, dual):
        return dual(math.cos(x[0]), -x[1]*math.sin(x[0]))
    elif isinstance(x, triple):
        return triple(math.cos(x[0]), -x[1]*math.sin(x[0]), -x[2]*math.sin(x[0]))
    else:
        return math.cos(x)

def log(x):
    if isinstance(x, dual):
        return dual(math.log(x[0]), x[1]/x[0])
    elif isinstance(x, triple):
        return triple(math.log(x[0]), x[1]/x[0], x[2]/x[0])
    else:
        return math.log(x)

def sqrt(x):
    return x**0.5

def cbrt(x):
    return x**(1/3)

