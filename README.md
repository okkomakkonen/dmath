# dmath

dmath is a Python package capable of dealing with dual numbers and automatic differentiation.

## Installation

Install this package by running the setup file in a terminal

```bash
$ pip install .
```

or by installing from git
```bash
$ pip install git+https://github.com/okkomakkonen/dmath.git
```

## Development

Using `pipenv` install all of the dev dependencies
```bash
$ pipenv install --dev
```
The tests can be run with
```bash
$ pipenv shell
$ coverage run -m pytest tests/
$ coverage report -m --omit=*/site-packages/*
```

## Usage

```python
>>> from dmath import grad, sin, cos
>>> f = lambda x: 3*x**2 + 1*x + 4
>>> grad(f)(3)
19.0
>>> g = lambda x, y: sin(x) * cos(y)
>>> grad(g)(2, 3)
(0.411982245665683, -0.12832006020245673)
```

## Todo

* `numpy` support
* C version
