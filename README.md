# dmath

Dmath is a Python package capable of dealing with dual numbers and automatic differentiation.

## Installation

Install this package by running the setup file in a terminal

```bash
pip install .
```

## Usage

```python
from dmath import grad

dmath.dual(3,1)  # Creates a dual number with real part 3 and infinitesimal part 1
f = lambda x: 3*x**2 + 1*x + 4  # Creates a polynomial w.r.t x
dmath.grad(f)(3)  # Calculates the derivative of the polynomial f at x=3
```
