import math
from itertools import zip_longest

# Types that are scalars in this context
_scalar = (int, float)


class dual:
    """Class for dual numbers with multiple infinitesimal parts

    Consult `wikipedia <https://en.wikipedia.org/wiki/Dual_number>`_
    for further information on dual numbers.
    """

    def __init__(self, *val):
        """Initializes the dual number or casts a scalar to a dual number

        Parameters
        ----------
        val : scalar or dual
            variable number of scalars or a single dual number

        Errors
        ------
        TypeError
            raises error when inputs are wrong type

        """
        if isinstance(val[0], dual) and len(val) == 1:
            self.val = val[0].val
        elif all([isinstance(a, _scalar) for a in val]):
            self.val = val
        else:
            raise TypeError

    @property
    def real(self):
        """Return real part
        """
        return self[0]

    @property
    def inft(self):
        """Return all infinitesimal parts
        """
        return tuple(self[1:])

    @property
    def dim(self):
        """Return dimension
        """
        return len(self.val)

    def __eq__(self, other):
        """Return the equality of the two numbers
        """
        other = dual(other)
        return all(a == b for a, b in zip_longest(self.val, other.val, fillvalue=0.0))

    def __repr__(self):
        """Return the string representation of the dual number in tuple format
        """
        return str(self.val)

    def __neg__(self):
        """Return the negation of the dual number
        """
        return dual(*[-a for a in self.val])

    def __add__(self, other):
        """Add two dual numbers, can take a scalar or a dual as input
        """
        other = dual(other)
        return dual(*[a + b for a, b in zip_longest(self.val, other.val, fillvalue=0)])

    def __iadd__(self, other):
        return self + other

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -(self - other)

    def __mul__(self, other):
        """Multiply self with a scalar or dual
        """
        if isinstance(other, _scalar):
            return dual(*[other*a for a in self.val])
        elif isinstance(other, dual):
            return dual(self[0] * other[0], *[other[0]*a + self[0]*b for a, b in zip_longest(self.val[1:], other.val[1:], fillvalue=0)])
        else:
            raise TypeError

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        """Perform division of dual numbers
        """
        return self*other**-1

    def __rtruediv__(self, other):
        return other*self**-1

    def __getitem__(self, index):
        return self.val[index]

    def __pow__(self, other):
        """Calculates the result of a dual number to the power of a dual number

        TODO: there is currently no way of calculating say 2**dual(3,1) since there is no method __rpow__ or similar,
            a possible solution is to create a new dmath.pow method that does it

            - Added a pow function.
            - It doesn't work


        Parameters
        ----------
        other : dual or scalar
            the power self is raised to

        Returns
        -------
        dual
            result of the raising

        """
        if isinstance(other, _scalar):
            val = self[0]**other
            return dual(val, *[val*a*other/self[0] for a in self.val[1:]])
        elif isinstance(other, dual):
            other = dual(other)
            val = self[0]**other[0]
            return dual(val, *[val*(a*other[0]/self[0] + b*math.log(self[0])) for a, b in zip_longest(self.val[1:], other.val[1:], fillvalue=0)])
        else:
            raise TypeError

    def __float__(self):
        return float(self[0])

    def __int__(self):
        return int(self[0])
