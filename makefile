init: purge
	python -m venv env
	env/bin/pip install --upgrade pip wheel setuptools
	env/bin/pip install -r requirements.txt
	env/bin/cythonize -i cython_example.pyx
	env/bin/python test_cython.py

purge:
	-@rm -rf env
	-@rm -rf build
	-@find . -type d -name '__pycache__' | xargs rm -r
	-@find . -type d -name '*.egg-info' | xargs rm -r
	-@find . -type f -name '*.pyc' | xargs rm -r
	-@find . -type f -name '*.so' | xargs rm -r
	-@find . -type d -name '*.ipynb_checkpoints' | xargs rm -r
	-@find . -type f -name '*.c' | xargs rm -r
