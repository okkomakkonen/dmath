from dmath import dual
import pytest


def test_init():

    with pytest.raises(TypeError):
        a = dual("hello")

    a = dual(3, 1)
    with pytest.raises(TypeError):
        b = dual(a, 4)


def test_real():
    assert dual(3, 1).real == 3


def test_inf():
    assert dual(1, 2, 3).inft == (2, 3)


def test_dim():
    assert dual(1, 2, 3).dim == 3


def test_eq():

    assert dual(3, 2) == dual(3, 2)
    assert dual(3) == 3
    assert dual(3, 1) != 3
    assert dual(3, 1) != dual(3)
    assert dual(3, 1) == dual(3, 1, 0)
    assert dual(3, 1) != dual(3, 1, 1)


def test_repr():

    assert repr(dual(3, 1)) == "dual(3, 1)"


def test_str():
    assert str(dual(3, 1)) == "(3, 1)"


def test_neg():
    assert -dual(3, 1) == dual(-3, -1)


def test_add():

    assert dual(3, 1) + dual(4, 1) == dual(7, 2)
    assert dual(3, 1) + dual(3, 1, 1) == dual(6, 2, 1)
    assert dual(3, 1) + 3 == dual(6, 1)
    assert 3 + dual(3, 1) == dual(6, 1)

    with pytest.raises(TypeError):
        dual(3, 1) + (4, 1)

    with pytest.raises(TypeError):
        (4, 1) + dual(3, 1)


def test_iadd():
    a = dual(3, 1)
    a += dual(4, 1)
    assert a == dual(7, 2)


def test_sub():
    assert dual(3, 1) - dual(4, 1) == dual(-1)
    assert dual(3, 1) - dual(3, 1, 1) == dual(0, 0, -1)
    assert dual(3, 1) - 2 == dual(1, 1)
    assert 2 - dual(3, 1) == dual(-1, -1)


def test_isub():
    a = dual(3, 1)
    a -= dual(4, 2)
    assert a == dual(-1, -1)


def test_mul():

    assert dual(3, 1) * dual(4, 1) == dual(12, 7)
    assert dual(3) * dual(5) == dual(15)
    assert 5 * dual(6, 2) == dual(30, 10)
    assert dual(4, 2) * 5 == dual(20, 10)

    with pytest.raises(TypeError):
        dual(3, 1) * (4, 2)

    with pytest.raises(TypeError):
        (4, 2) * dual(3, 1)


def test_imul():

    a = dual(3, 1)
    a *= dual(4, 1)
    assert a == dual(12, 7)


def test_truediv():

    assert dual(3, 1) / dual(4, 2) == dual(12 / 16, -2 / 16)
    assert dual(3, 1) / 3 == dual(1, 1 / 3)
    assert 3 / dual(3, 1) == dual(1, -1 / 3)

    with pytest.raises(TypeError):
        dual(3, 1) / (4, 2)

    with pytest.raises(TypeError):
        (4, 2) / dual(3, 1)


def test_itruediv():

    a = dual(3, 1)
    a /= dual(4, 2)
    assert a == dual(12 / 16, -2 / 16)


def test_pow():

    assert dual(3, 1) ** 2 == dual(3, 1) * dual(3, 1)
    assert dual(3, 1) ** 0.5 == dual(3 ** 0.5, 0.5 * 3 ** -0.5)
    assert 2 ** dual(3, 1) == dual(8, 5.545177444479562)

    with pytest.raises(TypeError):
        (4, 2) ** dual(3, 1)

    with pytest.raises(TypeError):
        dual(3, 1) ** (4, 2)


def test_ipow():

    a = dual(3, 1)
    a **= dual(4, 1)
    assert a == dual(3, 1) ** dual(4, 1)


def test_float():

    a = dual(3.5, 1.9)

    assert float(a) == 3.5
    assert isinstance(float(a), float)


def test_int():

    a = dual(3, 1)

    assert int(a) == 3
    assert isinstance(int(a), int)


def test_getitem():

    a = dual(3, 2, 1)

    assert a[0] == 3
    assert a[1] == 2
    assert a[2] == 1