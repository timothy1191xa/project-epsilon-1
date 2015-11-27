import numpy as np
from __future__ import division, print_function, absolute_import
from functools import reduce
from itertools import product
from t_test import *

def size(shape, axis=None):
    """
    Return the number of elements along a given axis.
    Parameters
    ----------
    shape : tuple
        The shape of the input array
    axis : int, optional
        Axis along which the elements are counted.  By default, give
        the total number of elements.
    Returns
    -------
    element_count : int
        Number of elements along the specified axis.
    """
    if axis is None:
        size = 1
        for e in shape:
            size *= e
        return size
    return shape[axis]


def get_increment(shape):
    """
    Return the increments corresponding to each axis or dimension in the shape.
    Parameters
    ----------
    shape : tuple
        The shape of the input array.
    Returns
    -------
    increment_per_axis : list
        The number of positions in the linear order that you need to move
        to retrieve the element specified by incrementing each axis
        in the corresponding index.
    """
    inc = [reduce(lambda x, y: x * y, shape[1 + i:], 1)
           for i in range(len(shape[1:]))]
    return inc + [1]


def get_index(shape, position):
    """
    Return the index in the multidimensional array that is corresponds to the
    element in the given position in the linear ordered.
    Parameters
    ----------
    shape : tuple
        The shape of the input array
    position : int
        The position in the linear ordering
    Returns
    -------
    index : tuple (same number of elements as shape)
        The index in the multidimensional array specified by the
        position in linear order
    """
    assert position < size(shape)
    inc = get_increment(shape)
    index = list()
    for i in inc:
        x = position // i
        position -= x * i
        index.append(x)
    return tuple(index)

def find_activated_voxel(shape, p):
    """
    Return the positions of the activated voxels based on the p-values we get from the t-test
    Parameters
    ----------
    shape : tuple
            The shape of the first dimension of our data
    p: numpy.ndarray
       The p values for our predictors and voxels
    Returns
    -------
    position : numpy.ndarray
        The index of our activated voxels
        position1...4 correspond to the cond001...4 .txt in model_one
    """
    loc1 = [i for i,j in enumerate(p[1,...]) if j < 0.05]
    loc2 = [i for i,j in enumerate(p[2,...]) if j < 0.05]
    loc3 = [i for i,j in enumerate(p[3,...]) if j < 0.05]
    loc4 = [i for i,j in enumerate(p[4,...]) if j < 0.05]

    position1 = []
    for i in loc1:
        position1.append(get_index(shape, i))

    position2 = []
    for i in loc2:
        position2.append(get_index(shape, i))

    position3 = []
    for i in loc3:
        position3.append(get_index(shape, i))

    position4 = []
    for i in loc4:
        position4.append(get_index(shape, i))


    position1 = np.asarray(position1)
    position2 = np.asarray(position2)
    position3 = np.asarray(position3)
    position4 = np.asarray(position4)


location_of_txt="../txt_files/"
np.savetxt(location_of_txt+'ds005_sub001_t1r1_position1.txt', position1)
np.savetxt(location_of_txt+'ds005_sub001_t1r1_position2.txt', position2)
np.savetxt(location_of_txt+'ds005_sub001_t1r1_position3.txt', position3)
np.savetxt(location_of_txt+'ds005_sub001_t1r1_position4.txt', position4)
