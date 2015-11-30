"""
Purpose:
-----------------------------------------------------------------------------------
BOLD image load for certain subject's certain run
-----------------------------------------------------------------------------------
"""


import numpy as np
import nibabel as nib

location_of_data="../../data/ds005/"


def load_img(subject_number, run_number):
	""" Return img_data in np.array

	Parameters
	----------
	subject_number : int
		Subject Number

	run_number : int
		run number
	
	Returns
	-------
	data : np.array
		the image data
		
	"""

	img=nib.load(location_of_data+'sub00%s/BOLD/task001_run00%s/bold.nii' %(subject_number, run_number))
	data=img.get_data()[...,4:]
	return data

