.PHONY: all clean coverage test

all: clean

clean:
	find . -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" | xargs rm -f

coverage:
	nosetests data/tests --with-coverage --cover-package=data/data.py

test:
	nosetests data/tests

verbose:
	nosetests -v data/tests
