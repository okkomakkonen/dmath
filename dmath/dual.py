import math
from itertools import zip_longest

scalar = (int, float)

class dual:
    """Class for dual numbers with multiple infinitesimal parts"""

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
        elif all([isinstance(a, scalar) for a in val]):
            self.val = val
        else:
            raise TypeError

        self.dim = len(self.val)

    def __eq__(self, other):
        """Returns the equality of the two numbers

        Parameters
        ----------
        other : dual or scalar
            a scalar is cast as a dual

        Returns
        -------
        bool
            True if the numbers are equal and False otherwise

        """
        other = dual(other)
        return all([a == b for a, b in zip_longest(self.val, other.val, fillvalue=0)])

    def __repr__(self):
        """Returns the string representation of the dual number"""
        return str(self.val)

    def __neg__(self):
        """Returns the negation of the dual number"""
        return dual(*[-a for a in self.val])

    def __add__(self, other):
        """Adds two dual numbers

        Parameters
        ----------
        other : scalar or dual
            a scalar is cast as a dual

        Returns
        -------
        dual
            the sum of the dual numbers self and other


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
        """Multiplies self with a scalar or dual

        Parameters
        ----------
        other : scalar or dual

        Returns
        -------
        dual
            the product of self and other

        Errors
        ------
        TypeError
            raises error when other is wrong type

        """
        if isinstance(other, scalar):
            return dual(*[other*a for a in self.val])
        elif isinstance(other, dual):
            return dual(self[0] * other[0], *[other[0]*a + self[0]*b for a, b in zip_longest(self.val[1:], other.val[1:], fillvalue=0)])
        else:
            raise TypeError

    def __rmul__(self, other):
        return self * other

    def __div__(self, other):
        return self*other**-1

    def __rdiv__(self, other):
        return other*self**-1

    def __getitem__(self, index):
        return self.val[index]

    def __pow__(self, other):
        if isinstance(other, scalar):
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

