""" 

Test linear_regression.py 

This is a test module.

It is designed to be run the with the "nose" testing package (via the
"nosetests" script.

Nose will look for any functions with "test" in their names, and run them.

Nose reports any errors, or any failures.

So we use the tests to check that the results of our function are (still) as we
expect.


"""


# Python 3 compatibility
from __future__ import absolute_import, division, print_function
import pandas as pd
import numpy as np
import numpy.linalg as npl
from numpy.testing import assert_almost_equal, assert_array_equal, assert_equal 
import sys, os, pdb

#Specicy the path for functions
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))
import linear_regression
from linear_regression import *

data_location = os.path.join(os.path.dirname(__file__), '../../../data/')


def test_load_data():
	""" tests whether the behavior data is loadede in data frame. 

	Testing on subject 2.
	"""
	run1 = pd.read_table(data_location+'ds005/sub002/behav/task001_run001/behavdata.txt')
	run2 = pd.read_table(data_location+'ds005/sub002/behav/task001_run002/behavdata.txt')
	run3 = pd.read_table(data_location+'ds005/sub002/behav/task001_run003/behavdata.txt')

	#append all the runs in one pandas data frame
	r=run1.append(run2)
	run_total=r.append(run3)


	run_total_array=run_total.as_matrix()

	test_array=load_data('002', data_location).as_matrix()
	assert_array_equal(run_total_array, test_array)





def test_linear_regression():


	# Create a data frame
	d = {'y' : pd.Series([95, 85, 80, 75, 70, 65, 60, 55, 50, 45], index=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']),
		 'x1' : pd.Series([85, 95, 70, 65, 70, 60, 64, 60, 51, 49], index=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']),
		 'x2' : pd.Series([10, 8.8, 8.4, 7.5, 7.4, 7.2, 7.0, 6.4, 5.3, 4], index=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']),
		 }


	df = pd.DataFrame(d)


	beta1, pvalues1 = linear_regression(df, 'y', 'x1')
	beta2, pvalues2 = linear_regression(df, 'y', 'x2')
	beta3, pvalues3 = linear_regression(df, 'y', 'x1', 'x2')


	expected_beta1 = np.array([ 0.69128736,  1.00610931]) # Calculated by hands
	expected_p1 = np.array([0.95669000991385234, 0.00082441892685309844]) # Calculated by hands
	expected_beta2 = np.array([ 2.92830189,  9.03773585]) # Calculated by hands
	expected_p2 = [0.64660353670191761, 1.2010523101013017e-05] # Calculated by hands
	expected_beta3 = np.array([-0.01554384,  0.20355359,  7.55525124]) # Calculated by hands
	expected_p3 = np.array([0.99826544217405555, 0.37237722050579208, 0.0049816157477362418]) # Calculated by hands

	assert_almost_equal(expected_beta1, beta1)
	assert_almost_equal(expected_p1, pvalues1)
	assert_almost_equal(expected_beta2, beta2)
	assert_almost_equal(expected_p2, pvalues2)
	assert_almost_equal(expected_beta3, beta3)
	assert_almost_equal(expected_p3, pvalues3)








