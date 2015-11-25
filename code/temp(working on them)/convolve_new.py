import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import numpy.linalg as npl
import scipy.stats
from scipy.stats import gamma


# You need to install hrf_estimation python package first!
# Run the following commands in Terminal
# pip install -U joblib
# pip install -U hrf_estimation


# We can use these gamma functions to construct a continuous function that is 
# close to the hemodynamic response we observe for a single brief event in the 
# brain.

def hrf(times):
     """ Return values for HRF at given times """
     # Gamma pdf for the peak
     peak_values = gamma.pdf(times, 6)
     # Gamma pdf for the undershoot
     undershoot_values = gamma.pdf(times, 12)
     # Combine them
     values = peak_values - 0.35 * undershoot_values
     # Scale max to 0.6
     return values / np.max(values) * 0.6


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

def produce_neural_prediction(task_fname, tr, n_trs):
    TR = 2
    n_vols = 240
    tr_times = np.arange(0, 30, TR)
    hrf_at_trs = hrf(tr_times)
    neural_prediction = events2neural(task_fname, TR, n_vols)
    all_tr_times = np.arange(n_vols) * TR
    
    return all_tr_times, neural_prediction





# # Compile the design matrix
# # First column is convolved regressor
# # Second column all ones
# design = np.ones((len(convolved), 2))

# design[:, 0] = convolved

# plt.imshow(design, aspect=0.1, interpolation='nearest', cmap='gray')


# # Reshape the 4D data to voxel by time 2D
# # Transpose to give time by voxel 2D
# # Calculate the pseudoinverse of the design
# # Apply to time by voxel array to get betas
# data_2d = np.reshape(data1, (-1, data.shape[-1]))

# betas = npl.pinv(design).dot(data_2d.T)


# # Tranpose betas to give voxels by 2 array
# # Reshape into 4D array, with same 3D shape as original data,
# # last dimension length 2
# betas_4d = np.reshape(betas.T, img.shape[:-1] + (-1,))


# # Show the middle slice from the first beta volume
# plt.imshow(betas_4d[:, :, 14, 0], interpolation='nearest', cmap='gray')


# # Show the middle slice from the second beta volume
# plt.imshow(betas_4d[:, :, 14, 1], interpolation='nearest', cmap='gray')








# task = np.loadtxt('cond001.txt')

# ons_durs = task[:, :2] / TR

# for onset, duration in ons_durs:
#     time_course[onset:onset + duration] = 1



# ######################


# n_trs = img.shape[-1]

# TR = 2


# time_course = events2neural('ds114_sub009_t2r1_cond.txt', TR, n_trs)



# data = data[..., 4:]
# time_course = time_course[4:]

# n_voxels = np.prod(data.shape[:-1])


# data_2d = np.reshape(data, (n_voxels, data.shape[-1]))

# correlations_1d = np.zeros((n_voxels,))

# # Loop over voxels filling in correlation at this voxel
# for i in range(n_voxels):
#     correlations_1d[i] = np.corrcoef(time_course, data_2d[i, :])[0, 1]

# # Reshape the correlations array back to 3D
# correlations = np.reshape(correlations_1d, data.shape[:-1])

