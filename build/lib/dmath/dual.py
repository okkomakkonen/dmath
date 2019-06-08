import math

scalar = (int, float)

class dual:

    def __init__(self, a, b=0):
        if isinstance(a, dual):
            self.val = a.val
        elif isinstance(a, scalar) and isinstance(b, scalar):
            self.val = (a, b)

    def __eq__(self, other):
        other = dual(other)
        try:
            return self.val == other.val
        except:
            return False

    def __repr__(self):
        return '({}+{}\u03B5)'.format(*self.val)

    def __neg__(self):
        return dual(-self[0], -self[1])

    def __add__(self, other):
        other = dual(other)
        return dual(self[0] + other[0], self[1] + other[1])

    def __iadd__(self, other):
        return self + other

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(-other)

    def __rsub__(self, other):
        return -self.__sub__(other)

    def __mul__(self, other):
        other = dual(other)
        return dual(self[0]*other[0], self[1]*other[0] + self[0]*other[1])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        pass
        other = dual(other)
        return self*dual(1/self[0], -self[1]/self[0]**2)

    def __getitem__(self, index):
        return self.val[index]

    def __pow__(self, other):
        other = dual(other)
        val = self[0]**other[0]
        return dual(val, val*(self[1]*other[0]/self[0] + other[1]*math.log(self[0])))

    def __float__(self):
        return float(self[0])

    def __int__(self):
        return int(self[0])

