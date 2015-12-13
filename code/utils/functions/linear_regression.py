""" Linear Regression on Begavioral data """


import pandas as pd
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "./"))
#import statsmodels.api as sm
import statsmodels.formula.api as smf
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import t 
import numpy.linalg as npl
import math
import logistic_reg
from logistic_reg import *





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

		print ("Can't find files in such directory! Please enter the directory where you store ds005 dataset!")
		return

	run_1=run1.append(run2)
	run_total=run_1.append(run3) #append all the data frames of run

	return(run_total)


"""
To combine all the behavioral data

Parameters:

	data_dir: The working directory that you store your data

Return:
	
	all_data: the behavioral data that contains 16 subjects, each subject has 3 runs

"""
def combine_all_data(data_dir = "/Users/macbookpro/Desktop/stat159_Project/"):

	# Get all the subjects
	all_subjects = ['001', '002', '003', '004', '005', '006', '007', 
	'008', '009', '010', '011', '012', '013', '014', '015', '016']

	all_data = []

	# Loop for 16 subjects to get the data
	for i in all_subjects:
		temp = load_data(i, data_dir)
		
		# if there's no such dataset, then stop running the loop and return nothing
		if temp is None:
			return

		# combine all the data
		all_data.append(temp)

	# Concat the data
	all_data = pd.concat(all_data)

	# Calculate the difference for future use
	all_data['diff'] = all_data['gain'] - all_data['loss']

	# Calculate the ratio for future use
	all_data['ratio'] = all_data['gain'] / all_data['loss']


	all_data['log_gain'] = np.log(all_data['gain'])

	all_data['log_loss'] = np.log(all_data['loss'])

	all_data['log_diff'] = np.log(all_data['diff'])

	all_data['log_ratio'] = np.log(all_data['ratio'])

	# # Remove the rows that have respcat == -1 
	#(meaning that the individual chooses to not participate the activity)
	all_data = all_data[np.logical_not(all_data['respcat'] == -1)]

	return (all_data)




def load_each_subject(data_dir = "/Users/macbookpro/Desktop/stat159_Project/"):

	all_subjects = ['001', '002', '003', '004', '005', '006', '007', 
	'008', '009', '010', '011', '012', '013', '014', '015', '016']

	l = []

	for i in all_subjects:
		l.append(load_data(i, data_dir))

	for i in range(len(all_subjects)):
		l[i]['ratio'] = l[i]['gain'] / l[i]['loss']

	return l



"""
To combine all the behavioral data

Parameters:

	data: The dataset that contains variables
	y: Dependent variable
	args: Explanatory variable(s)

"""
def linear_regression(data, y, *arg):

	# Get the length of data
	n = len(data)

	# Get the lenght of arg
	p = len(arg) + 1

	# manipulate the names of variables
	variables = []
	for i in range(p-1):
		variables.append(', data[arg['+str(i)+']]')

	# Get the coefficient matrix
	X = np.column_stack(( eval("np.ones(n)" + ''.join(variables)) ))
	Y = data[y]

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
	tvalues = []
	for i in range(p):
		tvalues.append(abs(beta[i] - 0)/ (math.sqrt(MRSS * npl.inv(X.T.dot(X))[i,i])) )

	# Calculate the p-values
	pvalues = [stats.t.sf(np.abs(i), df-1)*2 for i in tvalues]

	# Print out the betas and p-values
	for i in range(1,p):
		print('==============================================================')
		print(arg[i-1])
		print ('Coefficient: ' + str(beta[i]), 'p-value: ' + str(pvalues[i]))

	return beta, pvalues

"""
def linear_regression_RT_with_gain_and_loss(data):

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
"""



def linear_regression_fast(data, formula):
	#plt.plot(data['diff'], data['RT'], '+')
	# It seems like there's no siginificant relationship between diff and Response time
	# When we do the regression, it shows that difference between gain and loss does not really matter either.


	est = smf.ols(formula = formula, data=data).fit()
	est.summary()

	return est



def simple_regression_plot(data, dep_var, exp_var):
	y = data[dep_var]
	x = data[exp_var]
	n = len(data)
	# Design X matrix
	X = np.column_stack((np.ones(n), x))
	# Get the beta
	B = npl.pinv(X).dot(y)
	# Get the regression line
	x_vals = [0, max(x)]
	y_vals = [my_line(0), my_line(max(x))]
	# Plot the simple linear regression
	plt.plot(x, y, '+')
	plt.xlabel('ratio (gain/loss)')
	plt.ylabel('Response Time')
	plt.plot(x_vals, y_vals)
	plt.title('Ratio vs Response Time with predicted line')
	return



def beta_statistics():

	data = load_each_subject()

	betas = [0] * len(data)
	pvalues = [0] * len(data)

	for i in range(len(data)):
		betas[i], pvalues[i] = linear_regression(data[i], 'RT', 'gain', 'loss')

	lambdas = []

	for i in range(len(data)):
		lambdas.append( math.log(betas[i][2] / betas[i][1])    )

	return

def plot_neural_and_behav_loss_aversion(data, beta = None):

	all_subjects = ['001', '002', '003', '004', '005', '006', '007', 
	'008', '009', '010', '011', '012', '013', '014', '015', '016']

	lambdas = []
	loss_aversion = []

	for i in range(len(all_subjects)):

		a = add_gainlossratio(data[i])
		b = organize_columns(a)
		x = logit("respcat ~ gain + loss", b).fit()
		logit_pars = x.params
		ratio =  -logit_pars['loss'] / logit_pars['gain'] 
		lambdas.append( math.log(ratio) )
		loss_aversion.append( (-logit_pars['loss']) - logit_pars['gain'] ) # This will be changed!


	X = np.column_stack((np.ones(16), loss_aversion))


	
	B = npl.pinv(X).dot(lambdas)

	def my_line(x, B = B):
    	# Best prediction 
		return B[0] + B[1] * x
		
	x_vals = [0, max(loss_aversion)]
	y_vals = [my_line(0), my_line(max(loss_aversion))]

	plt.plot(loss_aversion, lambdas, '+') 
	plt.plot(x_vals, y_vals)

	#plt.xlabel('negative loss beta - gain beta')
	#plt.ylabel('log of lambda')
	
	plt.title("Scatterplot of correspondence between neural \nloss aversion and behavioral loss aversion")
	plt.xlabel(r'Neural loss aversion [-($\beta[loss]) - \beta[gain]$]')
	plt.ylabel(r'Behavioral loss aversion [ln($\lambda)$]')

	plt.show()

	return



