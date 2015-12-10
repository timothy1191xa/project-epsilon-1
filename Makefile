.PHONY: all clean coverage test verbose

all: clean

clean:
	find . -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" | xargs rm -f

coverage:
	nosetests data/tests code/utils/tests --with-coverage --cover-package=code/utils/functions --cover-package=data/data.py

test:
	nosetests data/tests code/utils/tests

verbose:
	nosetests data/tests code/utils/tests -v
