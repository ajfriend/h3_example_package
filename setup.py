from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize('src/h3vecex/cython_example.pyx')
)
