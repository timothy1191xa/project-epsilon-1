from __future__ import print_function  # print('me') instead of print 'me'
from __future__ import division  # 1/2 == 0.5, not 0
from __future__ import absolute_import
import scipy.stats
from scipy.stats import gamma
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib


# def plot_3D_bold_nii(data, color=False):
#     """
#     Plot all horizontal slices of 3D fMRI image at a given point in time.
#     Parameters:
#     -----------
#     data : np.ndarray
#         3D array of fMRI data
#     color: boolean
#         Turn on/off the color option
#     Return:
#     -------
#     Canvas of horizontal slices of the brain at a given time
#     """
#     length, width, depth = data.shape
#     len_side = int(np.ceil(np.sqrt(depth))) # Number slices per side of canvas
#     canvas = np.zeros((length * len_side, width * len_side))
#     depth_i = 0 # The ith slice with respect to depth
#     for row in range(len_side):
#         column = 0
#         while column < len_side and depth_i < depth:
#             canvas[length * row:length * (row + 1), width * column:width * (column + 1)] = data[..., depth_i]
#             depth_i += 1
#             column += 1
#     if color:
#         plt.imshow(canvas, interpolation="nearest")
#     else:
#         plt.imshow(canvas, interpolation="nearest", cmap="gray")
#     plt.colorbar()
#     return None


