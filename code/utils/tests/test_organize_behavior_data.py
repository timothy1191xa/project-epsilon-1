""" Tests for organize_behavior_data function in glm module
This checks the organize_behavior_data function.

Tests on our dataset (ds005) because other dataset doesn't have the behav data. 

Run at the tests directory with:
    nosetests code/utils/tests/test_organize_behavior_data.py

"""
# Loading modules.
import numpy as np
import numpy.linalg as npl
import nibabel as nib
import pandas as pd
import os, sys
from numpy.testing import assert_almost_equal, assert_array_equal, assert_equal, 
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))
from organize_behavior_data import *

project_location="../../../"
data_location=project_location+"data/ds005/"

def test_load_behav_txt():
	""" tests whether the function is properly taking out the errors in the subject's 
	responses. 

	Testing on subject 2.
	"""
	fixedshape = (248,7)
	behav1=np.loadtxt(data_location+'sub002/behav/task001_run001/behavdata.txt',skiprows=1)
	behav2=np.loadtxt(data_location+'sub002/behav/task001_run002/behavdata.txt',skiprows=1)
	behav3=np.loadtxt(data_location+'sub002/behav/task001_run003/behavdata.txt',skiprows=1)
	#concatenate them to be 1
	behav=np.concatenate((behav1,behav2,behav3),axis=0)

	#check if the shape is same
	assert_equal(load_behav_txt(2).shape,fixedshape)
	#check if there is any error is not taken out yet
	assert_equal(np.where(behav[:,5]==-1),np.array([]).reshape(1,0))


def test_load_behav_text_one():




def test_load_in_dataframe():

