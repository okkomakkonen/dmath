from .dual import dual

"""
def deriv(func):
    def derivative(x):
        return func(dual(x,1))[1]
    return derivative
"""

def grad(func):
    def gradient(*args):
        n = len(args)
        val = func(*[mdual(args[k], *[1 if i == k else 0 for i in range(n)]) for k in range(n)])
        return tuple([val[k] for k in range(1, n + 1)]) if n > 1 else val[1]
    return gradient