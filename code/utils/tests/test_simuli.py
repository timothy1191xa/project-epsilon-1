from __future__ import division  # 1/2 == 0.5, not 0
from __future__ import absolute_import
from __future__ import print_function  # print('me') instead of print 'me'

""" Test stimuli module
Run tests with::
    nosetests test_stimuli.py
"""

import numpy as np
import numpy.testing as npt
import scipy.stats
from scipy.stats import gamma
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib


import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../functions/"))

import stimuli

def test_hrf():
    peak_values = gamma.pdf(np.arange(0,24, 1.0/100),6)
    undershoot_values = gamma.pdf(np.arange(0,24,1.0/100), 12)
    values = peak_values - 0.35 * undershoot_values
    hrf = values/np.max(values) * 0.6 
    npt.assert_array_equal(hrf,hrf(np.arange(0,24,1.0/100)))
    


def test_events2neural():
    # test events2neural function
    neural = stimuli.events2neural('cond_test1.txt', 2, 16)
    # cond_test1.txt file is:
    """
    10    5.0    1
    20    4.0    2
    24    3.0    0.1
    """
    # Expected values for tr=2, n_trs=16
    expected = np.zeros(16)
    expected[5:7] = 1
    expected[10:12] = 2
    expected[12] = 0.1
    npt.assert_array_equal(neural, expected)
    neural = stimuli.events2neural('cond_test1.txt', 1, 30)
    # Expected values for tr=1, n_trs=30
    expected = np.zeros(30)
    expected[10:15] = 1
    expected[20:24] = 2
    expected[24:27] = 0.1
    npt.assert_array_equal(neural, expected)

def test_events2neural_high():
    """test with gain condition from subject 3's run 001

    """
    TR=2
    n_trs=240
    tr_div=100
    condfile = np.loadtxt("../../../data/ds005/sub003/model/model001/onsets/task001_run001/cond002.txt")
    onsets = condfile[:, 0]
    durations_seconds = condfile[:, 1]
    amplitudes = condfile[:, 2]
    onsets_in_scans = onsets_seconds / TR 
    high_res_times = np.arange(0, n_trs, 1.0/tr_div) * TR
    high_res_neural = np.zeros(high_res_times.shape)
    high_res_onset_indices = onsets_in_scans * tr_div
    high_res_durations = durations_seconds / TR * tr_div
    for hr_onset, hr_duration, amplitude in list(zip(high_res_onset_indices,high_res_durations,amplitudes)):
        hr_onset = int(round(hr_onset))
        hr_duration = int(round(hr_duration))
        high_res_neural[hr_onset:hr_onset+hr_duration] = amplitude

    test_high_res_times, test_high_res_neural = events2neural_high('../../../data/ds005/sub003/model/model001/onsets/task001_run001/cond002.txt')
    npt.assert_array_equal(high_res_times, test_high_res_times)
    npt.assert_array_equal(high_res_neural, test_high_res_neural)

