""" Linear Regression on Begavioral data """


import pandas as pd
#import statsmodels.api as sm
import statsmodels.formula.api as smf
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import t 
import numpy.linalg as npl
import math

%matplotlib





"""
Parameters:

	subject: 1 - 16
	data_dir: The working directory that you store your data

Return:
	
	run_total: the data for 3 runs

"""
def load_data(subject, data_dir = "/Users/macbookpro/Desktop/stat159_Project/"):
	
	# Get the directory where data is stored
	data_location= data_dir + 'ds005/sub' + subject

	try:

		# Load the data for each run
		run1 = pd.read_table(data_location+"/behav/task001_run001/behavdata.txt")
		run2 = pd.read_table(data_location+"/behav/task001_run002/behavdata.txt")
		run3 = pd.read_table(data_location+"/behav/task001_run003/behavdata.txt")

	except IOError:

		print "Can't find files in such directory! Please enter the directory where you store ds005 dataset!"
		return

	run_1=run1.append(run2)
	run_total=run_1.append(run3) #append all the data frames of run

	return(run_total)




def combine_all_data(data_dir = "/Users/macbookpro/Desktop/stat159_Project/"):

	all_subjects = ['001', '002', '003', '004', '005', '006', '007', 
	'008', '009', '010', '011', '012', '013', '014', '015', '016']

	all_data = []

	for i in all_subjects:
		temp = load_data(i, data_dir)
		
		if temp is None:
			return

		all_data.append(temp)

	return (pd.concat(all_data))



"""
Parameters:

	data

Return:
	
	run_total: the data for 3 runs

"""
def linear_regression(data):

	# Remove the rows that have respcat == -1 (meaning that the individual chooses to not participate
	# the activity)
	data = data[np.logical_not(data['respcat'] == -1)]

	# Calculate the difference
	data['diff'] = data['gain'] - data['loss']

	# Get the length of data
	n = len(data)

	# Get the coefficient matrix
	X = np.column_stack((np.ones(n), data['gain'], data['loss']))
	Y = data['RT']

	# Calculate the coefficients
	beta = npl.pinv(X).dot(Y)

 	# The fitted values - y hat
	fitted = X.dot(beta)

	# Residual error
	errors = Y - fitted

	# Residual sum of squares
	RSS = (errors**2).sum(axis=0) # (Y - X.dot(beta)).T.dot(Y - X.dot(beta))

	# Degrees of freedom
	df = X.shape[0] - npl.matrix_rank(X)

	# Mean residual sum of squares
	MRSS = RSS / df

	# Calculate t statistics
	t_intercept = abs(beta[0] - 0)/ (math.sqrt(MRSS * npl.inv(X.T.dot(X))[0,0])) 
	t_gain = abs(beta[1] - 0)/ (math.sqrt(MRSS * npl.inv(X.T.dot(X))[1,1])) 
	t_loss = abs(beta[2] - 0)/ (math.sqrt(MRSS * npl.inv(X.T.dot(X))[2,2]))

	# Calculate the p-values
	pval_intercept = stats.t.sf(np.abs(t_intercept), df-1)*2
	pval_gain = stats.t.sf(np.abs(t_gain), df-1)*2
	pval_loss = stats.t.sf(np.abs(t_loss), df-1)*2

	print('==============================================================')
	print('Gain:')
	print 'Coefficient: ' + str(beta[1]), 'p-value: ' + str(pval_gain)
	print('==============================================================')
	print('Loss:')
	print 'Coefficient: ' + str(beta[2]), 'p-value: ' + str(pval_loss)

	return


def linear_regression_fast(data):
	#plt.plot(data['diff'], data['RT'], '+')
	# It seems like there's no siginificant relationship between diff and Response time
	# When we do the regression, it shows that difference between gain and loss does not really matter either.




	est = smf.ols(formula='RT ~ diff', data=data).fit()
	est.summary()

	est = smf.ols(formula='RT ~ gain + loss', data=data).fit()



	est = smf.ols(formula='respcat ~ diff', data=data).fit()
	est = smf.ols(formula='respcat ~ gain + loss', data=data).fit()
	
	return







