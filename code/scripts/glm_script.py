import numpy as np
from glm import *
import nibabel as nib
import matplotlib.pyplot as plt

run convolution_normal_script.py
# run the convolution_normal_script.py script to get the design matrix X_matrix

#get 4_d image data
data_location = "../../data/ds005/sub002/BOLD/task001_run001/"
img = nib.load(data_location + "bold.nii")
data = img.get_data()

beta_4d = glm_multi(data[...,4:],X_matrix)
MRSS, fitted, residuals = glm_diagnostics(beta_4d, X_matrix, data[...,4:])

print ("MRSS of multiple regression: "+str(np.mean(MRSS)))
plt.plot(data[32,32,17], label = "actual")
plt.plot(fitted[32,32,17], label = "fitted")
plt.title("Subject 001, voxel (32,32,17) actual vs fitted")
plt.legend(loc = "upper left", fontsize = "smaller")
plt.savefig("glm_fitted.png")
plt.close()
