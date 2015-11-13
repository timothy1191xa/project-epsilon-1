"""take out the volumne outliers in an image"""

import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as npl
from itertools import product
import diagnostics
reload(diagnostics) 

img=nib.load('ds005/sub002/BOLD/task001_run001/bold.nii')
data=img.get_data()

"""get std"""
volstd = diagnostics.vol_std(data)
outliers_index, thres = diagnostics.iqr_outliers(volstd)









