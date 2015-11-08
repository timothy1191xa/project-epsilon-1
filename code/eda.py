import nibabel as nib 
import matplotlib.pyplot as plt
import numpy as np
img = nib.load('bold.nii')
data = img.get_data()

def meansd(data):
	nvol = data.shape[-1]
	means = []
	stds = []
	for i in range(nvol):
		means.append(np.mean(data[:,:,:,i]))
        	stds.append(np.std(data[:,:,:,i]))
	return means,stds

plt.plot(meansd(data)[0])
plt.xlabel('timepoints')
plt.ylabel('means')
plt.title('Mean of Signals')
plt.savefig('means.png')
plt.close()
plt.plot(meansd(data)[1])
plt.xlabel('timepoints')
plt.ylabel('standard deviations')
plt.title('Standard Deviations of Signals')
plt.savefig('stds.png')
plt.close()

task = np.loadtxt('cond001.txt')
TR = 2
ons_durs = task[:, :2] / TR
time_course = np.zeros(img.shape[-1])
for onset, duration in ons_durs:
    time_course[onset:onset + duration] = 1
is_task_tr = (time_course == 1)
is_rest_tr = (time_course == 0)
on_volumes = data[..., is_task_tr]
off_volumes = data[..., is_rest_tr]
plt.subplot(211)
plt.plot(meansd(on_volumes)[0])
plt.xlabel('timepoints')
plt.ylabel('means')
plt.title('Means of On Volumes')
plt.subplot(212)
plt.plot(meansd(off_volumes)[0])
plt.xlabel('timepoints')
plt.ylabel('means')
plt.title('Mean of Off Volumes')
plt.savefig('onoffmeans.png')
plt.close()
plt.subplot(211)
plt.plot(meansd(on_volumes)[1])
plt.xlabel('timepoints')
plt.ylabel('stds')
plt.title('Standard Deviations of On Volumes')
plt.subplot(212)
plt.plot(meansd(off_volumes)[1])
plt.xlabel('timepoints')
plt.ylabel('stds')
plt.title('Standard Deviations of Off Volumes')
plt.savefig('onoffstds.png')
plt.close()


behav = np.loadtxt('behavdata.txt')
response = behav[1:,-2]
is_accept_tr = (response == 1)
is_reject_tr = (response == 0)
accept_volumns = on_volumes[..., is_accept_tr]
reject_volumns = on_volumes[..., is_reject_tr]
plt.subplot(211)
plt.plot(meansd(accept_volumns)[0])
plt.xlabel('timepoints')
plt.ylabel('means')
plt.title('Mean of Accepted Signals')
plt.subplot(212)
plt.plot(meansd(reject_volumns)[0])
plt.xlabel('timepoints')
plt.ylabel('means')
plt.title('Mean of Rejected Signals')
plt.savefig('armeans.png')
plt.close()
plt.subplot(211)
plt.plot(meansd(accept_volumns)[1])
plt.xlabel('timepoints')
plt.ylabel('stds')
plt.title('Standard Deviations of Accepted Signals')
plt.subplot(212)
plt.plot(meansd(reject_volumns)[1])
plt.xlabel('timepoints')
plt.ylabel('stds')
plt.title('Standard Deviations of Rejected Signals')
plt.savefig('arstds.png')
plt.close()



