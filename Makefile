.PHONY: all clean coverage test verbose

all: clean

clean:
	find . -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" | xargs rm -f

coverage:
	nosetests code/utils/tests data/tests/ --with-coverage --cover-package=code/utils/functions,data/data_hashes.py,data/data.py,data/filtered_data_sh_script.py,data/get_data_hashes.py,data/get_ds005_hashes_from_txt.py

test:
	nosetests code/utils/tests data/tests/

verbose:
	nosetests data/tests code/utils/tests -v
