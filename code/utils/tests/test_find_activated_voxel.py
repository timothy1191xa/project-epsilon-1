import os
import sys
import numpy as np

import unittest
import itertools
import scipy.ndimage
from scipy.ndimage.filters import gaussian_filter
import matplotlib.pyplot as plt
import nibabel as nib
from numpy.testing import assert_almost_equal
from nose.tools import assert_not_equals


# Add path to functions to the system path.
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))

# Load smoothing function.
from find_activated_voxel_functions import *
project_path = os.path.join(os.path.dirname(__file__), '../../../')

def test_size():
    shape = (2, 3, 2)
    assert_equal(size(shape), 12)
    assert_equal(size(shape, axis=0),2)

def test_get_increment():
    assert_equal(get_increment((2, 4)),[4, 1])
    assert_equal(get_increment((2, 2, 2)),[4, 2, 1])

def test_get_index():
    shape = (2,)
    assert_equal(get_index(shape, 1), (1,))
    shape = (2, 2, 2)
    assert_equal(get_index(shape, 4),(1, 0, 0))
    assert_equal(get_index(shape, 2),(0, 1, 0))


