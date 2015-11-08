import numpy as np
import matplotlib.pyplot as plt
%matplotlib
import nibabel as nib

img = nib.load('bold.nii')
data = img.get_data()
data = data[..., 1:]
shape = data.shape
shape

meanval = []
for i in range(0,shape[3]):
    meanval.append(np.mean(data[...,i]))

stdval = []
for i in range(0,shape[3]):
    stdval.append(np.std(data[...,i]))
    

x = list(range(239))
y = meanval
coeff = np.polyfit(x, y, 2)
polynomial = np.poly1d(coeff)
xval = np.arange(1, 239, 1)
yval = polynomial(xval)
plt.plot(x, y)
plt.plot(xval,yval)
plt.ylabel('Mean MR signal')
plt.xlabel('timepoints')
plt.title('Mean signal (unfiltered)')
plt.savefig('Mean_signal.png')
plt.show()
plt.close()

x = list(range(239))
y2 = meanval
plt.plot(x, y2)
plt.ylabel('std MR signal')
plt.xlabel('timepoints')
plt.title('signal std')
plt.savefig('signal_std.png')
plt.show()
plt.close()


# code for calculating the median absolute deviation
def mad(data, axis=None):
    return np.mean(np.absolute(data - np.mean(data, axis)), axis)
mad(data)

        
import numpy as np
d = np.loadtxt('behavdata2.txt', delimiter="\t")
d.shape
ratio = []
gain = d[0:,1]
loss = d[0:,2]
ratio.append(gain/loss)
x3 = range(0,d.shape[0])
plt.xlim(min(x3)-10, max(x3)+10)
plt.ylim(min(gain)-10, max(gain)+10)
plt.plot(x3, gain,'r')
plt.plot(x3, loss,'b')
plt.plot(x3, np.asarray(ratio)[0],'k')
plt.savefig('behavdata.png')
plt.show()
plt.close()

np.asarray(ratio)[0]


plt.subplot(2,1,1)
x3 = range(0,d.shape[0])
plt.xlim(min(x3), max(x3)+10)
plt.ylim(0,9)
plt.plot(x3, np.asarray(ratio)[0],'r')


plt.subplot(2,1,2)
plt.xlim(0, data.shape[3]+10)
plt.ylim(153,157)
plt.plot(x, meanval,'b')
plt.savefig('compare.png')
plt.show()
plt.close()


#######
def vol_std(data):
    import numpy as np
    shape = data.shape
    std = []
    for i in range(0,shape[-1]):
        vol_1d = np.ravel(data[..., i])
        std.append(np.std(vol_1d))
    return(std)

    
def iqr_outliers(arr_1d, iqr_scale=1.5):
    import numpy as np
    centile25 = np.percentile(arr_1d, 25)
    centile75 = np.percentile(arr_1d, 75)
    iqr = centile75 - centile25
    high_thresold = centile75 + iqr_scale*iqr
    low_thresold = centile25 - iqr_scale*iqr
    thresholds = (low_thresold, high_thresold)
    outlier = []
    for i in arr_1d:
        if i <= low_thresold or i >= high_thresold:
            outlier.append(i)
        else:
            outlier.append(0)
    indices = np.nonzero(outlier)
    return (indices[-1], thresholds)

stan = vol_std(data)
indices = iqr_outliers(std, iqr_scale=1.5)[0]


