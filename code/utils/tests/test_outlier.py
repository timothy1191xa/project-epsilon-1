""" Tests for iqr_outliers function in diagnostics module

Run with:

    nosetests test_iqr_outliers
"""


""" Tests for vol_std function in diagnostics module

Run with:

    nosetests test_vol_std.py
"""

import numpy as np

from .. import outlier
from nose.tools import assert_equal
from numpy.testing import assert_almost_equal, assert_array_equal


def test_vol_std():
    # We make a fake 4D image
    shape_3d = (2, 3, 4)
    V = np.prod(shape_3d)
    T = 10  # The number of 3D volumes
    # Make a 2D array that we will reshape to 4D
    arr_2d = np.random.normal(size=(V, T))
    expected_stds = np.std(arr_2d, axis=0)
    # Reshape to 4D
    arr_4d = np.reshape(arr_2d, shape_3d + (T,))
    actual_stds = vol_std(arr_4d)
    assert_almost_equal(expected_stds, actual_stds)


def test_iqr_outliers():
    # Test with simplest possible array
    arr = np.arange(101)  # percentile same as value
    # iqr = 50
    exp_lo = 25 - 75
    exp_hi = 75 + 75
    indices, thresholds = iqr_outliers(arr)
    assert_array_equal(indices, [])
    assert_equal(thresholds, (exp_lo, exp_hi))
    # Reverse, same values
    indices, thresholds = iqr_outliers(arr[::-1])
    assert_array_equal(indices, [])
    assert_equal(thresholds, (exp_lo, exp_hi))
    # Add outliers
    arr[0] = -51
    arr[1] = 151
    arr[100] = 1  # replace lost value to keep centiles same
    indices, thresholds = iqr_outliers(arr)
    assert_array_equal(indices, [0, 1])
    assert_equal(thresholds, (exp_lo, exp_hi))
    # Reversed, then the indices are reversed
    indices, thresholds = iqr_outliers(arr[::-1])
    assert_array_equal(indices, [99, 100])
    assert_equal(thresholds, (exp_lo, exp_hi))


