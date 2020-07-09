from .dualnumbers import dual
from .functions import eps


def grad(func):
    """Return gradient of function.

    Given a scalar valued function with one or more scalar arguments,
    returns a function with the same signature as the original function.
    The new function returns a tuple with partial derivatives with respect to
    the original variables.
    """

    def gradient(*args):
        n = len(args)
        val = func(
            *[dual(args[k], *[1 if i == k else 0 for i in range(n)]) for k in range(n)]
        )
        return tuple(val[k] for k in range(1, n + 1)) if n > 1 else val[1]

    return gradient


def diff(func):
    """Return the derivative function of a given scalar valued function.
    """

    def deriv(arg):
        val = func(arg + eps(1))
        return val.inft[0]

    return deriv
