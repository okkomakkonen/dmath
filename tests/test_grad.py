from dmath import grad, sin, cos


def test_pol():
    def f(x):
        return x ** 2 + 3 * x + 6

    def f_prime(x):
        return 2 * x + 3

    assert grad(f)(3) == f_prime(3)


def test_trig():
    def g(x):
        return sin(x ** 2)

    def g_prime(x):
        return 2 * x * cos(x ** 2)

    assert grad(g)(6) == g_prime(6)


def test_grad():
    def f(x, y):
        return sin(x) * cos(y)

    def f_prime(x, y):
        return (cos(x) * cos(y), -sin(x) * sin(y))

    assert grad(f)(2, 3) == f_prime(2, 3)
