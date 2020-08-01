from dmath import grad
import math
import dmath
from pytest import approx


def range(lo, hi):
    diff = (hi - lo) / 12
    x = lo
    while x <= hi - diff:
        x += diff
        yield x


def test_exp():

    for x in range(-10, 10):
        assert dmath.exp(x) == math.exp(x) == grad(dmath.exp)(x)


def test_log():

    for x in range(1, 10):
        assert dmath.log(x) == math.log(x)
        assert grad(dmath.log)(x) == 1 / x


def test_sin():

    for x in range(-10, 10):
        assert dmath.sin(x) == math.sin(x)
        assert grad(dmath.sin)(x) == math.cos(x)


def test_cos():

    for x in range(-10, 10):
        assert dmath.cos(x) == math.cos(x)
        assert grad(dmath.cos)(x) == -math.sin(x)


def test_tan():

    for x in range(-10, 10):
        assert dmath.tan(x) == math.tan(x)
        assert grad(dmath.tan)(x) == approx(1 / math.cos(x) ** 2)


def test_asin():

    for x in range(-1, 1):
        assert dmath.asin(x) == math.asin(x)
        assert grad(dmath.asin)(x) == approx(1 / math.sqrt(1 - x ** 2))


def test_acos():

    for x in range(-1, 1):
        assert dmath.acos(x) == math.acos(x)
        assert grad(dmath.acos)(x) == approx(-1 / math.sqrt(1 - x ** 2))


def test_atan():

    for x in range(-10, 10):
        assert dmath.atan(x) == math.atan(x)
        assert grad(dmath.atan)(x) == approx(1 / (1 + x ** 2))


def test_sinh():

    for x in range(-10, 10):
        assert dmath.sinh(x) == math.sinh(x)
        assert grad(dmath.sinh)(x) == dmath.cosh(x)


def test_cosh():

    for x in range(-10, 10):
        assert dmath.cosh(x) == math.cosh(x)
        assert grad(dmath.cosh)(x) == math.sinh(x)


def test_tanh():

    for x in range(-10, 10):
        assert dmath.tanh(x) == math.tanh(x)
        assert grad(dmath.tanh)(x) == approx(1 / math.cosh(x) ** 2)


def test_asinh():

    for x in range(-10, 10):
        assert dmath.asinh(x) == math.asinh(x)
        assert grad(dmath.asinh)(x) == approx(1 / math.sqrt(x ** 2 + 1))


def test_acosh():

    for x in range(1, 10):
        assert dmath.acosh(x) == math.acosh(x)
        assert grad(dmath.acosh)(x) == approx(1 / math.sqrt(x ** 2 - 1))


def test_atanh():

    for x in range(-1, 1):
        assert dmath.atanh(x) == math.atanh(x)
        assert grad(dmath.atanh)(x) == approx(1 / (1 - x ** 2))


def test_sqrt():

    for x in range(0, 10):
        assert dmath.sqrt(x) == math.sqrt(x)
        assert grad(dmath.sqrt)(x) == approx(1 / (2 * math.sqrt(x)))
