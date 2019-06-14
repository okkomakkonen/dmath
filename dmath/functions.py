import math
from .dualnumbers import dual, scalar

pi = math.pi
e = math.e

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

def tan(x):
    if isinstance(x, dual):
        val = math.tan(x[0])
        deriv = 1/math.cos(x[0])**2
        return dual(val, *[deriv*a for a in x[1:]])
    else:
        return math.tan(x)

def acos(x):
    if isinstance(x, dual):
        val = math.acos(x[0])
        deriv = -1/math.sqrt(1-x[0]**2)
        return dual(val, *[deriv*a for a in x[1:]])
    else:
        return math.acos(x)

def asin(x):
    if isinstance(x, dual):
        val = math.asin(x[0])
        deriv = 1/math.sqrt(1-x[0]**2)
        return dual(val, *[deriv*a for a in x[1:]])
    else:
        return math.asin(x)

def atan(x):
    if isinstance(x, dual):
        val = math.atan(x[0])
        deriv = 1/(1 + x[0]**2)
        return dual(val, *[deriv*a for a in x[1:]])
    else:
        return math.atan(x)

# TODO: atan2, sinh, cosh, tanh, acosh, asinh, atanh

def sqrt(x):
    return x**0.5

def cbrt(x):
    return x**(1/3)

def pow(x, y):
    if isinstance(x, scalar) and isinstance(y, dual):
        return y.__rpow__(x)
    else:
        return x**y

