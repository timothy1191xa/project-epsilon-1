.PHONY: all clean coverage test verbose

all: clean

clean:
	find . -name "*.so" -o -name "*.pyc" -o -name "*.pyx.md5" | xargs rm -f

coverage:
	nosetests code/utils/tests data/tests/ --with-coverage --cover-package=code/utils/functions,data/data_hashes.py

test:
	nosetests code/utils/tests data/tests/

verbose:
	nosetests data/tests code/utils/tests -v

data:
	cd data && make data


linear:
	python code/stat159epsilon/code/utils/scripts/linear_regression_script.py

lostic:
	python code/stat159epsilon/code/utils/scripts/log_regression_script.py

t-test:
	python code/stat159epsilon/code/utils/scripts/t_test_plot_script.py

convolution-high:
	python code/stat159epsilon/code/utils/scripts/convolution_high_res_script.py

convolution-normal:
	python code/stat159epsilon/code/utils/scripts/convolution_normal_script.py

correlation:
	python code/stat159epsilon/code/utils/scripts/correlation_script

multi-comparison:
	python code/stat159epsilon/code/utils/scripts/multi_comparison_script.py

all-analysis:
	make linear
	make logistic
	make t-test
	make convolution-high
	make convolution-normal
	make correlation
	make multi-comparison
