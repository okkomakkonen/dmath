"""Implements a version of all functions in math package"""
import math
from .dualnumbers import dual, _scalar
from functools import wraps
from itertools import zip_longest

# Constants

pi = math.pi
e = math.e
tau = math.tau
inf = math.inf
nan = math.nan


def to_dmath(func, deriv):
    @wraps(func)
    def new_func(x):
        if isinstance(x, dual):
            val = func(x[0])
            der = deriv(x[0], val)
            return dual(val, *[der * a for a in x[1:]])
        else:
            return func(x)

    return new_func


exp = to_dmath(math.exp, lambda x, v: v)
log = to_dmath(math.log, lambda x, v: 1 / x)
sin = to_dmath(math.sin, lambda x, v: math.cos(x))
cos = to_dmath(math.cos, lambda x, v: -math.sin(x))
tan = to_dmath(math.tan, lambda x, v: v ** 2 + 1)
sqrt = to_dmath(math.sqrt, lambda x, v: 1 / (2 * v))
asin = to_dmath(math.asin, lambda x, v: 1 / math.sqrt(1 - x ** 2))
acos = to_dmath(math.acos, lambda x, v: -1 / math.sqrt(1 - x ** 2))
atan = to_dmath(math.atan, lambda x, v: 1 / (1 + x ** 2))
sinh = to_dmath(math.sinh, lambda x, v: math.cosh(x))
cosh = to_dmath(math.cosh, lambda x, v: math.sinh(x))
tanh = to_dmath(math.tanh, lambda x, v: 1 / math.cosh(x) ** 2)
asinh = to_dmath(math.asinh, lambda x, v: 1 / math.sqrt(x ** 2 + 1))
acosh = to_dmath(math.acosh, lambda x, v: 1 / math.sqrt(x ** 2 - 1))
atanh = to_dmath(math.atanh, lambda x, v: 1 / (1 - x ** 2))

log1p = to_dmath(math.log1p, lambda x, v: 1 / x)
log10 = to_dmath(math.log10, lambda x, v: 1 / (math.log(10) * x))
log2 = to_dmath(math.log2, lambda x, v: 1 / (math.log(2) * x))
expm1 = to_dmath(math.expm1, lambda x, v: v + 1)
erf = to_dmath(math.erf, lambda x, v: 2 / math.sqrt(math.pi) * math.exp(-(x ** 2)))
erfc = to_dmath(math.erfc, lambda x, v: -2 / math.sqrt(math.pi) * math.exp(-(x ** 2)))

prod = math.prod
isinf = math.isinf
isfinite = math.isfinite
isnan = math.isnan


def fsum(itr):
    if any(isinstance(i, dual) for i in itr):
        return dual(
            *(
                math.fsum(i)
                for i in zip_longest(*map(lambda x: dual(x).val, itr), fillvalue=0.0)
            )
        )
    else:
        return math.fsum(itr)


def pow(x, y):
    """Return x ** y"""
    if isinstance(x, _scalar) and isinstance(y, dual):
        return dual(x) ** y
    else:
        return x ** y


# Epsilons


def eps(n):
    return dual(*(0 for _ in range(n)), 1)
