import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from statsmodels.formula.api import logit, ols
import numpy.linalg as npl
import sys

#PREDICT SUBJECT's DECISION TO WHETHER GAMBLE OR NOT GIVEN WITH GAIN AND LOSS AMOUNT using LOGISTIC REGRESSION
#predictors : gain, loss, respnum


def add_gainlossratio(run):

	""" add gain/loss ratio column """

	gain = run.ix[:,1]
	loss = run.ix[:,2]
	run['ratio'] = gain/loss

	return run

def organize_columns(run):

	"""

	drop the unnecessary columns in the data frame,
	and reorganize the columns for logistic regression

	
	"""

	# drop onset column
	a = run.drop('onset', 1) 
	
	# drop PTval column
	run_organized = a.drop('PTval', 1) 

	# get the column names
	cols = run_organized.columns.tolist() 

	# put respcat column into front
	cols.insert(0, cols.pop(cols.index('respcat'))) 

	cols.insert(3, cols.pop(cols.index('ratio')))

	# reorganize
	run_organized = run_organized.reindex(columns= cols) 

	# drop error(rescap=-1) in experiment
	run_final = run_organized.drop(run_organized[run_organized.respcat == -1].index) 
	
	return run_final


def log_regression(run_final):

	"""do logistic regression on train cols to predict the subject's decision"""
	
	# do logistic regression
	x = logit("respcat ~ gain + loss", run_final).fit()

	# check the summary
	print(x.summary())

	#store the parameters of logistic regression
	logit_pars = x.params

	### START TO PLOT ###
	# calculate intercept and slope
	intercept = -logit_pars['Intercept'] / logit_pars['gain']
	slope = -logit_pars['loss'] / logit_pars['gain']

	fig = plt.figure(figsize = (10, 8))   

	# plot gain and loss for respcat = 1(decides to gamble)
	plt.plot(run_final[run_final['respcat'] == 1].values[:,2], run_final[run_final['respcat'] == 1].values[:,1], '.', label = "Gamble", mfc = 'None', mec='red')

	# plot gain and loss for respcat = 0(decides to not gamble)
	plt.plot(run_final[run_final['respcat'] == 0].values[:,2], run_final[run_final['respcat'] == 0].values[:,1], '.', label = "Not gamble", mfc = 'None', mec='blue')

	# draw regression line
	plt.plot(run_final['loss'], intercept + slope * run_final['loss'],'-', color = 'green') 

	plt.xlabel('Loss ($)')
	plt.ylabel('Gain ($)')
	plt.legend(loc='bottom right')
	plt.axis([2, 23, 8, 41])
	plt.title("Logistic Regression to predict 1(gamble) 0(not gamble) with gain and loss values\n")
	plt.savefig('log_regression.png')
	plt.show()
	return 


def plot_neural_and_behav_loss_aversion(data, subject):

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
		loss_aversion.append( (-logit_pars['loss']) - logit_pars['gain'] )

	X = np.column_stack((np.ones(16), loss_aversion))


	
	B = npl.pinv(X).dot(lambdas)

	def my_line(x):
    	# Best prediction 
		return B[0] + B[1] * x

	x_vals = [0, max(loss_aversion)]
	y_vals = [my_line(0), my_line(max(loss_aversion))]

	plt.plot(loss_aversion, lambdas, '+')
	plt.plot(x_vals, y_vals)

	plt.xlabel('negative loss beta - gain beta')
	plt.ylabel('log of lambda')

	plt.show()


	return






if __name__ == '__main__':
    a=add_gainlossratio(int(sys.argv[1]))
    b=organize_columns(a)
    log_regression(b)









