from setuptools import setup
from Cython.Build import cythonize

setup(
    name = 'h3_example_package',
    ext_modules = cythonize(
        'src/h3_example_package/geo.pyx',
        compiler_directives = {"language_level": "3"},
    ),
)

