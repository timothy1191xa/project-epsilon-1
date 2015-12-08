""" Logistic Regression on Begavioral data """

import sys, os
sys.path.append(".././utils")
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from logistic_reg import *
from organize_behavior_data import *



# Create the necessary directories if they do not exist
dirs = ['../../txt_output', '../../txt_output/conv_normal',\
        '../../fig','../../fig/log_reg_behav']
for d in dirs:
    if not os.path.exists(d):
            os.makedirs(d)

# Locate the different paths
#TODO: the current location for this file project-epsilon/code/scripts
project_path = '../../'
# TODO: change it to relevant path
data_path = project_path+'data/ds005/'

#change here to get your subject !
subject_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']

images_paths = ['ds005_sub' + s.zfill(3) +'_log_reg_behav' for s in subject_list]

for i,subject in enumerate(subject_list):
	behav_df = load_in_dataframe(subject)
	add_lambda = add_gainlossratio(behav_df)
	columns_changed = organize_columns(add_lambda)
	logit_pars = log_regression(columns_changed)

	### START TO PLOT ###
	# calculate intercept and slope
	intercept = -logit_pars['Intercept'] / logit_pars['gain']
	slope = -logit_pars['loss'] / logit_pars['gain']
	fig = plt.figure(figsize = (10, 8))   

	# plot gain and loss for respcat = 1(decides to gamble)
	plt.plot(behav_df[behav_df['respcat'] == 1].values[:,2], behav_df[behav_df['respcat'] == 1].values[:,1], '.', label = "Gamble", mfc = 'None', mec='red')

	# plot gain and loss for respcat = 0(decides to not gamble)
	plt.plot(behav_df[behav_df['respcat'] == 0].values[:,2], behav_df[behav_df['respcat'] == 0].values[:,1], '.', label = "Not gamble", mfc = 'None', mec='blue')

	# draw regression line
	plt.plot(behav_df['loss'], intercept + slope * behav_df['loss'],'-', color = 'green') 

	plt.xlabel('Loss ($)')
	plt.ylabel('Gain ($)')
	plt.legend(loc='bottom right')
	plt.axis([2, 23, 8, 41])
	plt.title("Subject_%s_Fitted Logistic Regression Line (1(gamble) 0(not gamble) with gain and loss values)\n"%(images_paths[i]))
	plt.savefig(dirs[3]+'/'+images_paths[i])
	plt.clf()


# behav_df = load_in_dataframe(3)
# a=add_gainlossratio(behav_df)
# b=organize_columns(a)
# log_regression(b)

