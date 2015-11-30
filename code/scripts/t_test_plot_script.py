import numpy as np
import sys
sys.path.append(".././utils")
from t_test import *
from find_activated_voxel_functions import *
from convolution_normal_script import X_matrix
import nibabel as nib
import matplotlib.pyplot as plt

location_of_data = "../../data/ds005/sub001/BOLD/task001_run001/"
location_of_plot = "../../plots/"

img = nib.load(location_of_data+ "bold.nii")
data = img.get_data()
beta, t, df,p=t_test(data,X_matrix)

shape = data.shape[:3]

t1 = np.reshape(t[1,:],shape)
for i in range(34):
 plt.subplot(5,7,i+1)
 plt.imshow(t1[:,:,i])
plt.savefig(location_of_plot+"t_statistics_for_condition_1")
plt.close()

t2 = np.reshape(t[2,:],shape)
for i in range(34):
 plt.subplot(5,7,i+1)
 plt.imshow(t2[:,:,i])
plt.savefig(location_of_plot+"t_statistics_for_condition_2")
plt.close()

t3 = np.reshape(t[3,:],shape)
for i in range(34):
 plt.subplot(5,7,i+1)
 plt.imshow(t3[:,:,i])
plt.savefig(location_of_plot+"t_statistics_for_condition_3")
plt.close()

t4 = np.reshape(t[4,:],shape)
for i in range(34):
 plt.subplot(5,7,i+1)
 plt.imshow(t4[:,:,i])
plt.savefig(location_of_plot+"t_statistics_for_condition_4")
plt.close()

