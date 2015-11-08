import numpy as np
import matplotlib.pyplot as plt
%matplotlib
import nibabel as nib

img = nib.load('bold.nii')
data = img.get_data()
data = data[..., 1:]
shape = data.shape
shape

datamean = np.mean(data, axis=-1)

#datamean[i, j, k] = np.max(datamean)
#plt.imshow(datamean[:, :, k], cmap='gray', interpolation='nearest')
#voxel_time_course = data[i, j, k]
#plt.plot(voxel_time_course)
#img.shape
