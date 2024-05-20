from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(
        'src/h3vecex/cython_example.pyx',
        compiler_directives = {"language_level": "3"}
    )
)

