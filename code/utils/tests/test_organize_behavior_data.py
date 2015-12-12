""" Tests for organize_behavior_data function in glm module
This checks the organize_behavior_data function.

Run at the tests directory with:
    nosetests code/utils/tests/test_organize_behavior_data.py

"""
# Loading modules.
import numpy as np
import numpy.linalg as npl
import nibabel as nib
import pandas as pd
import os, sys
from numpy.testing import assert_almost_equal, assert_array_equal
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))
from organize_behavior_data import *

def test_load_behav_txt():
	""" tests whether the function is properly taking out the errors in the subject's 
	responses. 

	"""
	actual



def test_load_behav_text_one():




def test_load_in_dataframe():

