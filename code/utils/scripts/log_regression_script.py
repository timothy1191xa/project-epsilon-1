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


a=add_gainlossratio(behav_df)
b=organize_columns(a)
log_regression(b)