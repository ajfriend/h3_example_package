from setuptools import setup
from Cython.Build import cythonize

setup(
    name = 'h3_example_package',
    version = '0.0.1',
    ext_modules = cythonize(
        'src/h3_example_package/geo.pyx',
        compiler_directives = {"language_level": "3"},
    ),
    # setup_requires=[
    #     'Cython',
    #     'h3==4.0.0b5',
    # ],
)
