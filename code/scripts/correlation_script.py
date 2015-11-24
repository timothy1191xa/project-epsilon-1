# - compatibility with Python 3
from __future__ import print_function  # print('me') instead of print 'me'
from __future__ import division  # 1/2 == 0.5, not 0
from __future__ import absolute_import

# - import common modules
import numpy as np
import matplotlib.pyplot as plt

# import events2neural from stimuli module
from stimuli import events2neural
import nibabel as nib

project_location="../"
data_location=project_location+"data/ds005/"

# Load the sub001 run001 image
img = nib.load(data_location+"sub001/BOLD/task001_run001/bold.nii")
data = img.get_data()

# Get the number of volumes
n_trs = img.shape[-1]

# Identify the TR (time between scans)
TR = 2

# Call the events2neural function to generate the on-off values for each volume
task = data_location+"sub001/model/model001/onsets/task001_run001/cond001.txt"
time_course = events2neural(task, TR, n_trs)

# Make a single brain volume-size array of all zero to hold the correlations
correlations = np.zeros(data.shape[:-1])

# Loop over all voxel indices on the first, then second, then third dimension
# Extract the voxel time courses at each voxel coordinate in the image
# Get the correlation between the voxel time course and neural prediction
# Fill in the value in the correlations array

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        for k in range(data.shape[2]):
            vox_values = data[i, j, k]
            correlations[i, j, k] = np.corrcoef(time_course, vox_values)[1, 0]

# Plot the middle slice of the third axis from the correlations array
# plt.imshow(correlations[:, :, 14])
