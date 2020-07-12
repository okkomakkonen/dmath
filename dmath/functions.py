"""Implements a version of all functions in math package"""
import math
from .dualnumbers import dual, _scalar
from functools import wraps

# Constants

pi = math.pi
e = math.e


def to_dmath(func, deriv):
    @wraps(func)
    def new_func(x):
        if isinstance(x, dual):
            val = func(x[0])
            der = deriv(x[0])
            return dual(val, *[der * a for a in x[1:]])
        else:
            return func(x)

    return new_func


exp = to_dmath(math.exp, math.exp)
log = to_dmath(math.log, lambda x: 1 / x)
sin = to_dmath(math.sin, math.cos)
cos = to_dmath(math.cos, lambda x: -math.sin(x))
tan = to_dmath(math.tan, lambda x: 1 / math.cos(x) ** 2)
asin = to_dmath(math.asin, lambda x: 1 / math.sqrt(1 - x ** 2))
acos = to_dmath(math.asin, lambda x: -1 / math.sqrt(1 - x ** 2))
atan = to_dmath(math.atan, lambda x: 1 / (1 + x ** 2))
sinh = to_dmath(math.sinh, math.cosh)
cosh = to_dmath(math.cosh, math.sinh)
tanh = to_dmath(math.tanh, lambda x: 1 / math.cosh(x) ** 2)
asinh = to_dmath(math.asinh, lambda x: 1 / math.sqrt(x ** 2 + 1))
acosh = to_dmath(math.acosh, lambda x: 1 / math.sqrt(x ** 2 - 1))
atanh = to_dmath(math.tanh, lambda x: 1 / (1 - x ** 2))
sqrt = to_dmath(math.sqrt, lambda x: 1 / (2 * math.sqrt(x)))


def pow(x, y):
    """Return the value of x to the y.

    """
    if isinstance(x, _scalar) and isinstance(y, dual):
        return dual(x) ** y
    else:
        return x ** y


# Epsilons


def eps(n):
    return dual(*(0 for _ in range(n)), 1)
