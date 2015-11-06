""" Script to run diagnostic analysis on FMRI run

The FMRI 'run' is a continuous collection of one or more 3D volumes.

A run is usually stored as a 4D NIfTI image.

In this case we are analyzing the 4D NIfTI image: "ds114_sub009_t2r1.nii"

Fill in the code necessary under the comments below.

As you are debugging, we suggest you run this script from within IPython, with
::

    run diagnosis_script.py

Remember, in IPython, that you will need to "reload" any modules that have
changed.  So, if you have imported your module like this:

    import diagnostics

Then you will need to run this before rerunning your script, to get the latest
version of the code.

    reload(diagnostics)

Before you submit your homework, don't forget to check this script also runs
correctly from the terminal, with::

    python diagnosis_script.py
"""

import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt
import numpy.linalg as npl
from itertools import product
import diagnostics
reload(diagnostics)
"""
* Load the image as an image object
* Load the image data from the image
* Drop the first four volumes, as we know these are outliers
"""
img = nib.load('ds114_sub009_t2r1.nii')
data = img.get_data()
data = data[...,4:]

"""
Use your vol_std function to get the volume standard deviation values for the
remaining 169 volumes.

Write these 169 values out to a text file.
*IMPORTANT* - this text file MUST be called 'vol_std_values.txt'
"""
volstd = diagnostics.vol_std(data)
fobj = open('vol_std_values.txt', 'wt')
for i in volstd:
    fobj.write(str(i) + '\n')
fobj.close()

"""
Use the iqr_outlier detection routine to get indices of outlier volumes.

Write these indices out to a text file.

*IMPORTANT* - this text file MUST be called 'vol_std_outliers.txt'
"""
outliers_index, thres = diagnostics.iqr_outliers(volstd)
fobj = open('vol_std_outliers.txt', 'wt')
for i in outliers_index:
    fobj.write(str(i) + '\n')
fobj.close()

"""
Plot all these on the same plot:

* The volume standard deviation values;
* The outlier points from the std values, marked on the plot with an 'o'
  marker;
* A horizontal dashed line at the lower IRQ threshold;
* A horizontal dashed line at the higher IRQ threshold;

Extra points for a good legend to the plot.

Save the figure to the current directory as ``vol_std.png``.

IMPORTANT - use exactly this name.
"""
plt.plot(volstd,'r', label='volume sd values')
for i in outliers_index:
	plt.plot(i,volstd[i],'o',color='b')
plt.axhline(y=thres[0], color='g',ls='dashed',label='low threshold')
plt.axhline(y=thres[1], color='black',ls='dashed',label='high threshold')
plt.legend(loc=4)
plt.savefig('vol_std.png')
plt.clf()


""" Next calculate and plot the RMS difference values

* Calculate the RMS difference values for the image data;
* Use the ``iqr_outlier`` function to return indices of possible outliers in
  this RMS difference vector;

On the same plot, plot the following:

* The RMS vector;
* The identified outlier points marked with an `o` marker;
* A horizontal dashed line at the lower IRQ threshold;
* A horizontal dashed line at the higher IRQ threshold;

IMPORTANT - save this plot as ``vol_rms_outliers.png``
"""

rmsd = diagnostics.vol_rms_diff(data)
outliers_rms_index, thres_rms = diagnostics.iqr_outliers(rmsd)

plt.plot(rmsd,'r', label='rms differences values')
for i in outliers_rms_index:
	plt.plot(i,rmsd[i],'o', color='blue')
plt.axhline(y=thres_rms[0], color='g',ls='dashed',label='low threshold')
plt.axhline(y=thres_rms[1], color='black',ls='dashed',label='high threshold')
plt.legend(loc=1)
plt.xlabel('volume')
plt.ylabel('rms difference')
plt.savefig('vol_rms_outliers.png')
plt.clf()

""" Use the ``extend_diff_outliers`` to label outliers

Use ``extend_diff_outliers`` on the output from ``iqr_outliers`` on the RMS
difference values.  This gives you indices for labeled outliers.

On the same plot, plot the following:

* The RMS vector with a 0 appended to make it have length the same as the
  number of volumes in the image data array;
* The identified outliers shown with an `o` marker;
* A horizontal dashed line at the lower IRQ threshold;
* A horizontal dashed line at the higher IRQ threshold;

IMPORTANT - save this plot as ``extended_vol_rms_outliers.png``
"""
outliers_rms_label = diagnostics.extend_diff_outliers(outliers_rms_index)
rmsd_append = np.append(rmsd,0)

plt.plot(rmsd_append,'r', label='rms extended differences values')
for i in outliers_rms_label:
	plt.plot(i,rmsd_append[i],'o', color='blue')
plt.axhline(y=thres_rms[0], color='g',ls='dashed',label='low threshold')
plt.axhline(y=thres_rms[1], color='black',ls='dashed',label='high threshold')
plt.legend(loc=3)
plt.xlabel('volume')
plt.ylabel('rms difference')
plt.savefig('extended_vol_rms_outliers.png')
plt.clf()


""" Write the extended outlier indices to a text file.

IMPORTANT: name the text file extended_vol_rms_outliers.txt
"""

fobj = open('extended_vol_rms_outliers.txt', 'wt')
for i in outliers_rms_label:
    fobj.write(str(i) + '\n')
fobj.close()

""" Show that the residuals drop when removing the outliers

Create a design matrix for the image data with the convolved neural regressor
and an intercept column (column of 1s).

Load the convolved neural time-course from ``ds114_sub009_t2r1_conv.txt``.

Fit this design to estimate the (2) betas for each voxel.

Subtract the fitted data from the data to form the residuals.

Calculate the mean residual sum of squares (MRSS) at each voxel (the sum of
squared divided by the residual degrees of freedom).

Finally, take the mean of the MRSS values across voxels.  Print this value.
"""
convolved = np.loadtxt('ds114_sub009_t2r1_conv.txt')
convolved = convolved[4:]
N = len(convolved)
X = np.ones((N, 2))
X[:, 0] = convolved
Xp = npl.pinv(X)
Y = np.reshape(data, (-1, data.shape[-1]))
beta=np.dot(Xp,Y.T)
betas_4d = np.reshape(beta.T, img.shape[:-1] + (-1,))
Y_hat=np.dot(betas_4d, X.T)
df=X.shape[0]-npl.matrix_rank(X)
diff=data-Y_hat
residual=np.sum(diff**2)/df
residual=residual/np.product(data.shape[:-1])
print(residual)



"""
lst=[]
for i in np.shape(data[...,-1]):
	lst.append(range(i))
data_index=list(product(*lst))
beta=[]
for i in data_index:
	beta.append(Xp.dot(data[i]))
fitted=[]
for i in beta:
	fitted.append(X.dot(i))
errors=[]
for i in range(data_index):
	errors.append(data[data_index[i]]-fitted[i])
residual=[]
for i in errors:
	residual.append(np.sum(i ** 2)/(X.shape[0] - npl.matrix_rank(X)))
print(mean(residual))
"""

"""
Next do the exactly the same, except removing the extended RMS difference
outlier volumes from the data and the corresponding rows for the design.

Print the mean of the RMSS values across voxels. Is this value smaller?
"""
convolved_extend = np.delete(convolved, outliers_rms_label, 0)
N = len(convolved_extend)
X = np.ones((N, 2))
X[:, 0] = convolved_extend
Xp = npl.pinv(X)
data_extend = np.delete(data, outliers_rms_label,3)
Y = np.reshape(data_extend, (-1, data_extend.shape[-1]))
beta=np.dot(Xp,Y.T)
betas_4d = np.reshape(beta.T, img.shape[:-1] + (-1,))
Y_hat=np.dot(betas_4d, X.T)
df=X.shape[0]-npl.matrix_rank(X)
diff=data_extend-Y_hat
residual_extend=np.sum(diff**2)/df
residual_extend=residual_extend/np.product(data.shape[:-1])
print(residual_extend)


"""
Y_hat=np.dot(X,beta)
Y_hat=Y_hat.T
Y_hat=Y_hat.reshape(np.shape(data_extend)[0],np.shape(data_extend)[1],np.shape(data_extend)[2],np.shape(data_extend)[3])
df=X.shape[0]-npl.matrix_rank(X)
diff=data_extend-Y_hat
residual_extend=np.sum(diff**2)/df
residual_extend=residual_extend/np.shape(data_extend)[3]
print(residual_extend)
"""


""" Now save these two mean MRSS values to a text file

IMPORTANT: save to ``mean_mrss_vals.txt``
"""
fobj = open('mean_mrss_vals.txt', 'wt')
fobj.write("residual = " + str(residual) + '\n')
fobj.write("residual_extend = " + str(residual_extend) + '\n')
fobj.close()


# Some final checks that you wrote the files with their correct names
from os.path import exists
assert exists('vol_std_values.txt')
assert exists('vol_std_outliers.txt')
assert exists('vol_std.png')
assert exists('vol_rms_outliers.png')
assert exists('extended_vol_rms_outliers.png')
assert exists('extended_vol_rms_outliers.txt')
assert exists('mean_mrss_vals.txt')
