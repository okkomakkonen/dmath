import math
from .dualnumbers import dual, _scalar

# Constants

pi = math.pi
e = math.e

# Exponential


def exp(x):
    """Return the value exp(x)

    """
    if isinstance(x, dual):
        val = math.exp(x[0])
        deriv = val
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.exp(x)


def log(x):
    """Return the logarithm of x.

    """
    if isinstance(x, dual):
        val = math.log(x[0])
        deriv = 1 / x[0]
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.log(x)


# Trigonometric


def sin(x):
    """Return sine function of x.

    """
    if isinstance(x, dual):
        val = math.sin(x[0])
        deriv = math.cos(x[0])
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.sin(x)


def cos(x):
    """Return cosine function of x.

    """
    if isinstance(x, dual):
        val = math.cos(x[0])
        deriv = -math.sin(x[0])
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.cos(x)


def tan(x):
    """Return tangent function of x.

    """
    if isinstance(x, dual):
        val = math.tan(x[0])
        deriv = 1 / math.cos(x[0]) ** 2
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.tan(x)


# Inverse trigonometric


def acos(x):
    """Return the inverse cosine of x.

    """
    if isinstance(x, dual):
        val = math.acos(x[0])
        deriv = -1 / math.sqrt(1 - x[0] ** 2)
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.acos(x)


def asin(x):
    """Return the inverse sine of x.

    """
    if isinstance(x, dual):
        val = math.asin(x[0])
        deriv = 1 / math.sqrt(1 - x[0] ** 2)
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.asin(x)


def atan(x):
    """Return the inverse tangent of x.

    """
    if isinstance(x, dual):
        val = math.atan(x[0])
        deriv = 1 / (1 + x[0] ** 2)
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.atan(x)


# Hyperbolic


def sinh(x):
    """Return the hyperbolic sine of x.

    """
    if isinstance(x, dual):
        val = math.sinh(x[0])
        deriv = math.cosh(x[0])
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.sinh(x)


def cosh(x):
    """Return the hyperbolic cosine of x.

    """
    if isinstance(x, dual):
        val = math.cosh(x[0])
        deriv = math.sinh(x[0])
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.cosh(x)


def tanh(x):
    """Return the hyperbolic tangent of x.

    """
    if isinstance(x, dual):
        val = math.tanh(x[0])
        deriv = math.cosh(x[0]) ** -2
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.tanh(x)


# Inverse hyperbolic


def asinh(x):
    """Return the inverse hyperbolic sine of x.

    """
    if isinstance(x, dual):
        val = math.asinh(x[0])
        deriv = 1 / math.sqrt(x[0] ** 2 + 1)
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.asinh(x)


def acosh(x):
    """Return the inverse hyperbolic cosine of x.

    """
    if isinstance(x, dual):
        val = math.acosh(x[0])
        deriv = 1 / math.sqrt(x[0] ** 2 - 1)
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.acosh(x)


def atanh(x):
    """Return the inverse hyperbolic tangent of x.

    """
    if isinstance(x, dual):
        val = math.atanh(x[0])
        deriv = 1 / (1 - x[0] ** 2)
        return dual(val, *[deriv * a for a in x[1:]])
    else:
        return math.atanh(x)


# Roots


def sqrt(x):
    """Return the square root of x.

    """
    return x ** 0.5


def cbrt(x):
    """Return the cube root of x.

    """
    return x ** (1 / 3)


# Powers


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
