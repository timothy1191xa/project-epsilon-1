"""
Purpose:
-----------------------------------------------------------------------------------
Check the voxels that are activated over the experiment and compare between 
subject 1 and subject 3
-----------------------------------------------------------------------------------
"""


from __future__ import division, print_function, absolute_import
import numpy as np
import sys
sys.path.append(".././utils")
import nibabel as nib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from t_test import *
from find_activated_voxel_functions import *
from find_activated_voxel_script import position1, position2, position3, position4
from convolution_high_res_script import X_matrix_high_res
from load_BOLD import *
from affine import *


location_of_mni = '../../data/ds005_2/'