
"""
Purpose:
-----------------------------------------------------------------------------------
We generate convolved hemodynamic neural prediction into seperated txt files for 
all four conditions (task, gain, lost, distance), and also generate plots for 4 
BOLD signals over time for each of them too. 

Steps:
-----------------------------------------------------------------------------------
1. Extract 4 conditions of subject 1's first run
2. Load the data to get the 4th dimension shape
3. Convolve with hrf
4. Plot sampled HRFs with the high resolution neural time course
5. Save the convolved data into txt files
"""

import sys
sys.path.append(".././utils")
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from stimuli import *
from scipy.stats import gamma
from organize_behavior_data import *
from load_BOLD import *

location_of_data="../../data/ds005/"
location_of_model="ds005/sub00`/model/model001/onsets/task001_run001/"
location_of_plot="../../plots/"
location_of_txt="../txt_files/"


# Extract 4 conditions of subject 1's first run
task, gain, loss, dist = load_model_one(1,1)

# load data (subject 1 run 1 for now) ( you can change it if you want )
data = load_img(1,1)


TR = 2.0
tr_times = np.arange(0, data.shape[2], TR)
hrf_at_trs = hrf(tr_times)
n_vols = data.shape[-1]
X_matrix = np.ones((n_vols,5)) #design matrix (1 at the 0th column)


# create the matrix using np.convolve and plot them
all_tr_times = np.arange(data.shape[-1]) * TR
condition = [task, gain, loss, dist]
condition_string = ['task', 'gain', 'loss', 'dist']
for i,name in enumerate(condition):
	neural_prediction = events2neural(name,TR,n_vols)
	convolved = np.convolve(neural_prediction, hrf_at_trs)
	convolved = convolved[:-(len(hrf_at_trs)-1)]
	plt.plot(all_tr_times, neural_prediction)
	plt.plot(all_tr_times, convolved)
	plt.xlabel("time")
	plt.ylabel("HRF")
	plt.title("Condition %s"%(condition_string[i]))
	plt.savefig(location_of_plot+"convolved_%s.png"%(condition_string[i]))
	plt.clf()
	np.savetxt(location_of_txt+'ds005_sub001_t1r1_conv%s.txt'%(i+1), convolved)
	X_matrix[:,i+1] = convolved

# Your X_matrix is ready



