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


def load_data(subject, data_dir = "/Users/macbookpro/Desktop/stat159_Project/"):
	
	"""
	Parameters:

		subject: 1 - 16
		data_dir: The working directory that you store your data

	Return:
		
		run_total: the data for 3 runs

	"""
	# Get the directory where data is stored
	data_location = data_dir + 'ds005/sub' + subject

	# Load the data for each run
	run1 = pd.read_table(data_location+"/behav/task001_run001/behavdata.txt")
	run2 = pd.read_table(data_location+"/behav/task001_run002/behavdata.txt")
	run3 = pd.read_table(data_location+"/behav/task001_run003/behavdata.txt")


	run_1=run1.append(run2)
	run_total=run_1.append(run3) #append all the data frames of run

	return(run_total)



def linear_regression(data, y, *arg):
	"""
	To perform linear regression

	Parameters:

		data: The dataset that contains variables
		y: Dependent variable
		args: Explanatory variable(s)

	Return:
		beta: The coefficients for explantatory variables
		pvalues: The pvalues for each explantatory variables

	"""
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
	This is a function to generate simple regression plot

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


	This is the function that is undone - 	

	def plot_neural_and_behav_loss_aversion(all_subjects, data, beta = None):

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

	fig = plt.figure()
	ax = fig.add_subplot(111)

	plt.plot(loss_aversion, lambdas, '+') 
	plt.plot(x_vals, y_vals)
	
	plt.title("Scatterplot of correspondence between neural \nloss aversion and behavioral loss aversion")
	plt.xlabel(r'Neural loss aversion [-($\beta[loss]) - \beta[gain]$]')
	plt.ylabel(r'Behavioral loss aversion [ln($\lambda)$]')

	plt.grid()
	plt.show()

	return
"""







