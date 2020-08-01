from dmath import grad
import math
import dmath
from pytest import approx
from dmath import dual


def range(lo, hi):
    diff = (hi - lo) / 12
    x = lo
    while x <= hi - diff:
        x += diff
        yield x


def test_constants():

    assert dmath.pi == math.pi
    assert dmath.e == math.e
    assert dmath.tau == math.tau
    assert dmath.inf == math.inf
    assert dmath.nan is math.nan


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


def test_log1p():

    for x in range(0, 0.1):
        assert dmath.log1p(x) == math.log1p(x)
        assert grad(dmath.log1p)(x) == 1 / x


def test_log10():

    for x in range(0, 10):
        assert dmath.log10(x) == math.log10(x)
        assert grad(dmath.log10)(x) == approx(1 / (math.log(10) * x))


def test_log2():

    for x in range(0, 10):
        assert dmath.log2(x) == math.log2(x)
        assert grad(dmath.log2)(x) == approx(1 / (math.log(2) * x))


def test_expm1():

    for x in range(0, 0.1):
        assert dmath.expm1(x) == math.expm1(x)
        assert grad(dmath.expm1)(x) == math.expm1(x) + 1.0


def test_erf():

    for x in range(-10, 10):
        assert dmath.erf(x) == math.erf(x)
        assert grad(dmath.erf)(x) == 2 / math.sqrt(math.pi) * math.exp(-(x ** 2))


def test_erfc():

    for x in range(-10, 10):
        assert dmath.erfc(x) == math.erfc(x)
        assert grad(dmath.erfc)(x) == -2 / math.sqrt(math.pi) * math.exp(-(x ** 2))
