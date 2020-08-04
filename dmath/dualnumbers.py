"""
Implements a simple dual number class
"""

from math import log
from itertools import zip_longest
import numbers

# Types that are scalars in this context
_scalar = (int, float)


class dual(numbers.Number):
    """Class for dual numbers with multiple infinitesimal parts

    Consult `wikipedia <https://en.wikipedia.org/wiki/Dual_number>`_
    for further information on dual numbers.
    """

    __slots__ = ("_val",)

    def __new__(cls, *val):
        """Initializes the dual number or casts a scalar to a dual number"""

        self = super(dual, cls).__new__(cls)

        if len(val) == 1 and isinstance(val[0], dual):
            self._val = val[0]._val
        elif all(isinstance(a, _scalar) for a in val):
            self._val = val
        else:
            raise TypeError("val has to be dual or scalar")

        return self

    @property
    def val(self):
        return self._val

    def __hash__(self):
        if self.real == self:
            return hash(self[0])
        return hash(self.val)

    @property
    def real(self):
        """Returns the real part"""
        return self[0]

    @property
    def inft(self):
        """Returns all infinitesimal parts"""
        return tuple(self[1:])

    @property
    def dim(self):
        """Returns dimension"""
        return len(self.val)

    def __eq__(self, other):
        """Returns the equality of the two numbers"""
        other = dual(other)
        return all(a == b for a, b in zip_longest(self.val, other.val, fillvalue=0))

    def __repr__(self):
        """Returns the representation of the dual number"""
        return f"dual({', '.join(map(str, self.val))})"

    def __str__(self):
        """Returns the string of the dual number"""
        return str(self.val)

    def __neg__(self):
        """Returns -self"""
        return dual(*(-a for a in self.val))

    def __add__(self, other):
        """Returns self + other"""
        if isinstance(other, _scalar):
            return dual(self[0] + other, *self[1:])
        elif isinstance(other, dual):
            return dual(
                *(a + b for a, b in zip_longest(self.val, other.val, fillvalue=0))
            )
        else:
            return NotImplemented

    __radd__ = __iadd__ = __add__

    def __sub__(self, other):
        """Returns self - other"""
        return self + (-other)

    def __rsub__(self, other):
        """Returns other - self"""
        return -(self - other)

    __isub__ = __sub__

    def __mul__(self, other):
        """Returns self * other"""
        if isinstance(other, _scalar):
            return dual(*(other * a for a in self.val))
        elif isinstance(other, dual):
            return dual(
                self[0] * other[0],
                *(
                    other[0] * a + self[0] * b
                    for a, b in zip_longest(self.val[1:], other.val[1:], fillvalue=0)
                ),
            )
        else:
            return NotImplemented

    __rmul__ = __imul__ = __mul__

    def __truediv__(self, other):
        """Returns self / other"""
        if isinstance(other, _scalar):
            return 1 / other * self
        elif isinstance(other, dual):
            return self * other ** -1
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        """Returns other / self"""
        if isinstance(other, _scalar):
            return other * self ** -1
        else:
            return NotImplemented

    __itruediv__ = __truediv__

    def __getitem__(self, index):
        """Returns a component of the dual number"""
        return self.val[index]

    def __pow__(self, other):
        """Returns self ** other"""
        if isinstance(other, _scalar):
            val = self[0] ** other
            return dual(val, *(val * a * other / self[0] for a in self.val[1:]))
        elif isinstance(other, dual):
            val = self[0] ** other[0]
            return dual(
                val,
                *(
                    val * (a * other[0] / self[0] + b * log(self[0]))
                    for a, b in zip_longest(self.val[1:], other.val[1:], fillvalue=0)
                ),
            )
        else:
            return NotImplemented

    __ipow__ = __pow__

    def __rpow__(self, other):
        """Returns other ** self"""
        if isinstance(other, _scalar):
            val = other ** self[0]
            return dual(val, *(val * a * log(other) for a in self.val[1:]),)
        else:
            return NotImplemented

    def __float__(self):
        """Returns the float value of the first coordinate"""
        return float(self[0])

    def __int__(self):
        """Returns the int value of the first coordinate"""
        return int(self[0])
