
"""
Purpose:
-----------------------------------------------------------------------------------
We generate convolved hemodynamic neural prediction into seperated txt files for 
all four conditions (task, gain, lost, distance), and also generate plots for 4 
BOLD signals over time for each of them too. We use events2neural_high() in stimuli
because the onsets of condition do not start at TR.

Steps:
-----------------------------------------------------------------------------------
1. Extract 4 conditions of subject 1's first run
2. Gain higher time resolutions
3. Convolve with hrf
4. Plot sampled HRFs with the high resolution neural time course
5. Save to txt files
"""

import sys
sys.path.append(".././utils")
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from stimuli import *
from scipy.stats import gamma
from organize_behavior_data import *

location_of_data="../../data/ds005/"
location_of_model="ds005/sub001/model/model001/onsets/task001_run001/" 
location_of_plot="../../plots/"
location_of_txt="../txt_files/"


# Extract 4 conditions of subject 1's first run
task, gain, loss, dist = load_model_one(1,1)


# Gain higher time resolutions
high_res_times, high_task = events2neural_high(task)
_, high_gain = events2neural_high(gain)
_, high_loss = events2neural_high(loss)
_, high_dist = events2neural_high(dist)


# Convolve with hrf
hrf_times = np.arange(0,24,1.0/10)
hrf_at_hr = hrf(hrf_times)
high_res_hemo_task = np.convolve(high_task, hrf_at_hr)[:len(high_task)]
high_res_hemo_gain = np.convolve(high_gain, hrf_at_hr)[:len(high_gain)]
high_res_hemo_loss = np.convolve(high_loss, hrf_at_hr)[:len(high_loss)]
high_res_hemo_dist = np.convolve(high_dist, hrf_at_hr)[:len(high_dist)]

# Plot sampled HRFs with the high resolution neural time course
plt.plot(high_res_times, high_res_hemo_task)
plt.xlabel('Time (seconds)')
plt.ylabel('High resolution convolved task_condition')
plt.savefig(location_of_plot+'task_high_res_convolution')
plt.clf()

plt.plot(high_res_times, high_res_hemo_gain)
plt.xlabel('Time (seconds)')
plt.ylabel('High resolution convolved gain_condition')
plt.savefig(location_of_plot+'gain_high_res_convolution')
plt.clf()

plt.plot(high_res_times, high_res_hemo_loss)
plt.xlabel('Time (seconds)')
plt.ylabel('High resolution convolved loss_condition')
plt.savefig(location_of_plot+'loss_high_res_convolution')
plt.clf()

plt.plot(high_res_times, high_res_hemo_dist)
plt.xlabel('Time (seconds)')
plt.ylabel('High resolution convolved dist_condition')
plt.savefig(location_of_plot+'dist_high_res_convolution')
plt.clf()

# Save convolved information into txt files
np.savetxt(location_of_txt+'ds005_sub001_t1r1_conv1.txt', high_res_hemo_task)
np.savetxt(location_of_txt+'ds005_sub001_t1r1_conv2.txt', high_res_hemo_gain)
np.savetxt(location_of_txt+'ds005_sub001_t1r1_conv3.txt', high_res_hemo_loss)
np.savetxt(location_of_txt+'ds005_sub001_t1r1_conv4.txt', high_res_hemo_dist)

# plt.plot(all_tr_times1, neural_prediction1, color = 'blue', label='Task')
# plt.plot(all_tr_times2, neural_prediction2, color = 'red', label='Parametric gain')
# plt.plot(all_tr_times3, neural_prediction3, color = 'green', label='Parametric loss')
# plt.plot(all_tr_times4, neural_prediction4, color = 'black', label='Distance from indifference')
# plt.legend(loc='top left')
# plt.xlabel('Time(s)')
# plt.ylabel('Condition')
# plt.title("Neural Prediction")
# plt.savefig('neural_prediction.png')
# plt.clf()

# n_to_remove = len(hrf_at_trs) - 1


# convolved1 = np.convolve(neural_prediction1, hrf_at_trs)
# convolved2 = np.convolve(neural_prediction2, hrf_at_trs)
# convolved3 = np.convolve(neural_prediction3, hrf_at_trs)
# convolved4 = np.convolve(neural_prediction4, hrf_at_trs)

# convolved1 = convolved1[:-n_to_remove]
# convolved2 = convolved2[:-n_to_remove]
# convolved3 = convolved3[:-n_to_remove]
# convolved4 = convolved4[:-n_to_remove]

# plt.plot(all_tr_times1, neural_prediction1)
# plt.plot(all_tr_times1, convolved1)
# plt.title("Convolution_task")
# plt.savefig('convolution_task.png')
# plt.clf()
# plt.plot(all_tr_times2, neural_prediction2)
# plt.plot(all_tr_times2, convolved2)
# plt.title("Convolution_gain")
# plt.savefig('convolution_gain.png')
# plt.clf()
# plt.plot(all_tr_times3, neural_prediction3)
# plt.plot(all_tr_times3, convolved4)
# plt.title("Convolution_loss")
# plt.savefig('convolution_loss.png')
# plt.clf()
# plt.plot(all_tr_times4, neural_prediction4)
# plt.plot(all_tr_times4, convolved4)
# plt.title("Convolution_dist")
# plt.savefig('convolution_dist.png')





