# `h3_example_package`

An example repo for building a Python package on top of the `h3-py` Cython API.

We hope this example will empower users to customize `h3-py` to their needs,
without having the hassle of building all the `h3-py` code from scratch.

Example projects:

- supply a set of vectorized `h3-py` functions
- a different approach to the `h3-py` API

# Remote installation

A user should be able to install this package remotely with commands like:

```
pip install --upgrade pip wheel setuptools
pip install cython h3==4.0.0b5
pip install git+https://github.com/ajfriend/h3_example_package
```

Note: This is still a WIP, and the above commands will be simplified to a single `pip install`.

# Local installation and development

Check the `makefile`.

# TODOs

- generally improve/modernize build
- use `pyproject.toml`
- add examples of how a library developer would build wheels for a project like this and publish to PyPI
