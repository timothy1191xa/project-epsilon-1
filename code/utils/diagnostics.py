""" Diagnostics.py

A collection of utility functions for diagnostics on FMRI data

See test_* functions in this directory for nose tests
"""

import numpy as np
import pdb

def vol_std(data):
    """ Return standard deviation across voxels for 4D array `data`

    Parameters
    ----------
    data : 4D array
        4D array from FMRI run with last axis indexing volumes.  Call the shape
        of this array (M, N, P, T) where T is the number of volumes.

    Returns
    -------
    std_values : array shape (T,)
        One dimensonal array where ``std_values[i]`` gives the standard
        deviation of all voxels contained in ``data[..., i]``.
    """
    std_values = [np.std(np.ravel(data[...,i])) for i in range(0, np.shape(data)[3])]
    return np.array(std_values)

def iqr_outliers(arr_1d, iqr_scale=1):
    """ Return indices of outliers identified by interquartile range

    Parameters
    ----------
    arr_1d : 1D array
        One-dimensional numpy array, from which we will identify outlier
        values.
    iqr_scale : float, optional
        Scaling for IQR to set low and high thresholds.  Low threshold is given
        by 25th centile value minus ``iqr_scale * IQR``, and high threshold id
        given by 75 centile value plus ``iqr_scale * IQR``.

    Returns
    -------
    outlier_indices : array
        Array containing indices in `arr_1d` that contain outlier values.
    lo_hi_thresh : tuple
        Tuple containing 2 values (low threshold, high thresold) as described
        above.
    """
    # Hint : np.lookfor('centile')
    # Hint : np.lookfor('nonzero')
    sevenfifth = np.percentile(arr_1d,75)
    twenfifth = np.percentile(arr_1d,25)
    iqr = sevenfifth-twenfifth
    low = twenfifth-iqr_scale*iqr
    hi = iqr_scale*iqr+sevenfifth
    outliers1 = np.array(np.nonzero(arr_1d > hi))[0]
    outliers2 = np.array(np.nonzero((arr_1d < low)))[0]
    outliers = np.hstack((outliers1,outliers2))
    outliers.sort()
    return outliers,(low, hi)

def vol_rms_diff(arr_4d):
    """ Return root mean square of differences between sequential volumes

    Parameters
    ----------
    data : 4D array
        4D array from FMRI run with last axis indexing volumes.  Call the shape
        of this array (M, N, P, T) where T is the number of volumes.

    Returns
    -------
    rms_values : array shape (T-1,)
        One dimensonal array where ``rms_values[i]`` gives the square root of
        the mean (across voxels) of the squared difference between volume i and
        volume i + 1.
    """
    
    rms_values=[]
    for i in range(arr_4d.shape[-1]-1):
        diff_vol = arr_4d[...,i+1] - arr_4d[...,i]
        rms_values.append(np.sqrt(np.mean(diff_vol ** 2)))
    return np.array(rms_values)

def extend_diff_outliers(diff_indices):
    """ Extend difference-based outlier indices `diff_indices` by pairing

    Parameters
    ----------
    diff_indices : array
        Array of indices of differences that have been detected as outliers.  A
        difference index of ``i`` refers to the difference between volume ``i``
        and volume ``i + 1``.

    Returns
    -------
    extended_indices : 
        Array where each index ``j`` in `diff_indices has been replaced by two
        indices, ``j`` and ``j+1``, unless ``j+1`` is present in
        ``diff_indices``.  For example, if the input was ``[3, 7, 8, 12, 20]``,
        ``[3, 4, 7, 8, 9, 12, 13, 20, 21]``.
    """
    i=0
    while (i < len(diff_indices)):
        if i is (len(diff_indices)-1):
            diff_indices = np.insert(diff_indices,i+1,diff_indices[i]+1)
            break
        if diff_indices[i+1] == (diff_indices[i]+1):
            i=i+1
            continue
        diff_indices = np.insert(diff_indices,i+1,diff_indices[i]+1)
        i=i+2
    return diff_indices


