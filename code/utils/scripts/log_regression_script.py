"""
Purpose:
-----------------------------------------------------------------------------------
We try to capture the significance of gain and loss amount condition for each subjects.
We fit the logistic regression line based on their responses on the experiment. The slope 
of the fitted line illustrates the subject's sensitivity on either gain or loss amount. 

This script outputs plots for each subject and combine them into one image of subplots. 
-----------------------------------------------------------------------------------
Step:
1. 
"""

from __future__ import absolute_import, division, print_function
import sys, os
#TODO : later change this
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from logistic_reg import *
from organize_behavior_data import *



# Create the necessary directories if they do not exist
dirs = ['../../../fig','../../../fig/log_reg_behav']
for d in dirs:
    if not os.path.exists(d):
            os.makedirs(d)

# Locate the different paths
#TODO: the current location for this file project-epsilon/code/scripts
project_path = '../../../'
# TODO: change it to relevant path
data_path = project_path+'data/ds005/'
subject_list = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']

images_paths = ['ds005_sub' + s.zfill(3) +'_log_reg_behav' for s in subject_list]
