try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="dmath",
    description="Module for math with dual numbers including automatic differentiation",
    version="0.0.1",
    packages=["dmath"],
    author="Okko Makkonen",
    test_suite="tests",
)
