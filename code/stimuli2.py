""" Functions to work with standard OpenFMRI stimulus files

The functions have docstrings according to the numpy docstring standard - see:

    https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
"""

import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib


def events2neural(task_fname, tr, n_trs):
    """ Return predicted neural time course from event file `task_fname`

    Parameters
    ----------
    task_fname : str
        Filename of event file
    tr : float
        TR in seconds
    n_trs : int
        Number of TRs in functional run

    Returns
    -------
    time_course : array shape (n_trs,)
        Predicted neural time course, one value per TR
    """
    task = np.loadtxt(task_fname)
    # Check that the file is plausibly a task file
    if task.ndim != 2 or task.shape[1] != 3:
        raise ValueError("Is {0} really a task file?", task_fname)
    # Convert onset, duration seconds to TRs
    task[:, :2] = task[:, :2] / tr
    # Neural time course from onset, duration, amplitude for each event
    time_course = np.zeros(n_trs)
    for onset, duration, amplitude in task:
        time_course[onset:onset + duration] = amplitude
    return time_course

def events2neural_corr(cond_data, TR=2, n_trs=240, tr_divs=10):
   onsets_seconds = cond_data[:, 0]
   durations_seconds = cond_data[:, 1]
   amplitudes = cond_data[:, 2]
   onsets_in_scans = onsets_seconds / TR
   #We want a resolution to the 10th between each TR
   high_res_times = np.arange(0, n_trs, 1 / tr_divs) * TR
   high_res_neural = np.zeros(high_res_times.shape)
   high_res_onset_indices = onsets_in_scans * tr_divs
   high_res_durations = durations_seconds / TR * tr_divs
   for hr_onset, hr_duration, amplitude in zip(
              high_res_onset_indices, high_res_durations, amplitudes):
	          hr_onset = int(round(hr_onset))  # index - must be int
		      hr_duration = int(round(hr_duration))  # makes index - must be int
		          high_res_neural[hr_onset:hr_onset + hr_duration] = amplitude


