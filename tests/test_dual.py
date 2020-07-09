from dmath import dual


def test_eq():

    assert dual(3, 2) == dual(3, 2)
    assert dual(3) == 3
    assert dual(3, 1) != 3
    assert dual(3, 1) == dual(3, 1, 0)
    assert dual(3, 1) != dual(3, 1, 1)


def test_add():

    assert dual(3, 1) + dual(4, 1) == dual(7, 2)
    assert dual(3, 1) + dual(3, 1, 1) == dual(6, 2, 1)
    assert dual(3, 1) + 3 == dual(6, 1)
    assert 3 + dual(3, 1) == dual(6, 1)


def test_mul():

    assert dual(3, 1) * dual(4, 1) == dual(12, 7)
    assert dual(3) * dual(5) == dual(15)
    assert 5 * dual(6, 2) == dual(30, 10)
    assert dual(4, 2) * 5 == dual(20, 10)
