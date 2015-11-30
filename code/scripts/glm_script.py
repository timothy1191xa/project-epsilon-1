import sys
sys.path.append(".././utils")
import numpy as np
from glm import *
from convolution_normal_script import X_matrix
import nibabel as nib
import matplotlib.pyplot as plt


location_of_plot = "../../plots/"
location_of_data = "../../data/ds005/sub001/BOLD/task001_run001/"

#get 4_d image data
img = nib.load(location_of_data+ "bold.nii")
data = img.get_data()

beta_4d = glm_multi(data[...,4:],X_matrix)
MRSS, fitted, residuals = glm_diagnostics(beta_4d, X_matrix, data[...,4:])

print ("MRSS of multiple regression: "+str(np.mean(MRSS)))
plt.plot(data[4,22,11], label = "actual")
plt.plot(fitted[4,22,11], label = "fitted")
plt.title("Subject 001, voxel (4,22,11) actual vs fitted")
plt.legend(loc = "upper left", fontsize = "smaller")
plt.savefig(location_of_plot + "glm_fitted.png")
plt.close()
