init: purge
	python -m venv env
	env/bin/pip install --upgrade pip wheel setuptools
	env/bin/pip install -r requirements.txt

local_install: init
	env/bin/pip install .
	make test

remote_install: init
	env/bin/pip install git+https://github.com/ajfriend/h3_example_package
	make test

purge:
	-@rm -rf env build .pytest_cache
	-@find . -type d -name '__pycache__' | xargs rm -r
	-@find . -type d -name '*.egg-info' | xargs rm -r
	-@find . -type f -name '*.pyc' | xargs rm -r
	-@find . -type f -name '*.so' | xargs rm -r
	-@find . -type d -name '*.ipynb_checkpoints' | xargs rm -r
	-@find . -type f -name '*.c' | xargs rm -r

test:
	env/bin/pytest



