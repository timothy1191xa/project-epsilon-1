
"""
Purpose:
-----------------------------------------------------------------------------------
Get the position of an image in millimeters in the space. 

Steps:
-----------------------------------------------------------------------------------

"""

import numpy as np
import numpy.linalg as npl
import nibabel as nib

def voxel_to_mm(voxel_fname, coordinate):
    """ Return the coordinate's location in the image in millimeters (MNI coordinate)

    Parameters
    ----------
    voxel_fname : str
        Filename of event file (use standard brain (mni))
    coordinate : list of tuples
    	Voxel coordinates

    Returns
    -------
    location_mm : list
        location in millimeters

    """
    img = nib.load(voxel_fname)

    #test image shape here

    vox_to_mm = img.affine
    location_mm = []
    for i in coordinate:
    	location_mm.append(nib.affines.apply_affine(vox_to_mm, i))
    return location_mm


def mm_to_voxels(voxel_fname, mm):
	""" Return the voxel coordinate (inverse of the above function)

    Parameters
    ----------
    voxel_fname : str
        Filename of event file (use standard brain (mni))
    mm : list
    	coordinate in mm (MNI coordinate)

    Returns
    -------
    voxel : list
    	voxel coordinate

    """
	img = nib.load(voxel_fname)	
	mm_to_vox = npl.inv(img.affine)
	voxel = []
	for i in mm:
		voxel.append(nib.affines.apply_affine(mm_to_vox, mm))
	return voxel