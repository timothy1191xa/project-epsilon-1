script.

import sys
sys.path.append(".././utils")
from logistic_reg import *
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
from stimuli import events2neural
from scipy.stats import gamma

TR = 2
n_vols = 240
tr_times = np.arange(0, 30, TR)
hrf_at_trs = hrf(tr_times)


all_tr_times1, neural_prediction1 = produce_neural_prediction('../../data/ds005/sub001/model/model001/onsets/task001_run001/cond001.txt', TR, n_vols)	
all_tr_times2, neural_prediction2 = produce_neural_prediction('../../data/ds005/sub001/model/model001/onsets/task001_run001/cond002.txt', TR, n_vols)		
all_tr_times3, neural_prediction3 = produce_neural_prediction('../../data/ds005/sub001/model/model001/onsets/task001_run001/cond003.txt', TR, n_vols)		
all_tr_times4, neural_prediction4 = produce_neural_prediction('../../data/ds005/sub001/model/model001/onsets/task001_run001/cond004.txt', TR, n_vols)	



plt.plot(all_tr_times1, neural_prediction1, color = 'blue', label='Task')
plt.plot(all_tr_times2, neural_prediction2, color = 'red', label='Parametric gain')
plt.plot(all_tr_times3, neural_prediction3, color = 'green', label='Parametric loss')
plt.plot(all_tr_times4, neural_prediction4, color = 'black', label='Distance from indifference')
plt.legend(loc='top left')
plt.xlabel('Time(s)')
plt.ylabel('Condition')
plt.title("Neural Prediction")
plt.savefig('neural_prediction.png')
plt.clf()

n_to_remove = len(hrf_at_trs) - 1


convolved1 = np.convolve(neural_prediction1, hrf_at_trs)
convolved2 = np.convolve(neural_prediction2, hrf_at_trs)
convolved3 = np.convolve(neural_prediction3, hrf_at_trs)
convolved4 = np.convolve(neural_prediction4, hrf_at_trs)

convolved1 = convolved1[:-n_to_remove]
convolved2 = convolved2[:-n_to_remove]
convolved3 = convolved3[:-n_to_remove]
convolved4 = convolved4[:-n_to_remove]

plt.plot(all_tr_times1, neural_prediction1)
plt.plot(all_tr_times1, convolved1)
plt.title("Convolution_task")
plt.savefig('convolution_task.png')
plt.clf()
plt.plot(all_tr_times2, neural_prediction2)
plt.plot(all_tr_times2, convolved2)
plt.title("Convolution_gain")
plt.savefig('convolution_gain.png')
plt.clf()
plt.plot(all_tr_times3, neural_prediction3)
plt.plot(all_tr_times3, convolved4)
plt.title("Convolution_loss")
plt.savefig('convolution_loss.png')
plt.clf()
plt.plot(all_tr_times4, neural_prediction4)
plt.plot(all_tr_times4, convolved4)
plt.title("Convolution_dist")
plt.savefig('convolution_dist.png')


np.savetxt('ds005_sub001_t1r1_conv1.txt', convolved1)
np.savetxt('ds005_sub001_t1r1_conv2.txt', convolved2)
np.savetxt('ds005_sub001_t1r1_conv3.txt', convolved3)
np.savetxt('ds005_sub001_t1r1_conv4.txt', convolved4)


