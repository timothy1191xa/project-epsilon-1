"""
This will be your new module with the Pearson correlation function

First try to fill in the "pearson_1d" function.

When you are done with "pearson_1d", you should be able to run the following
command (from the day5 directory) and see no errors or failures::

    nosetests test_pearson_1d.py

Then, if you are feeling brave, fill in the "pearson_2d" function.  Test with::

    nosetests test_pearson_2d.py
"""
# Python 3 compatibility
from __future__ import print_function, division

import numpy as np


def pearson_1d(x, y):
    """ Pearson product-moment correlation of vectors `x` and `y`

    Parameters
    ----------
    x : array shape (N,)
        One-dimensional array to correlate with `y`
    y : array shape (N,)
        One dimensional array to correlate with `x`

    Returns
    -------
    r_xy : scalar
        Pearson product-moment correlation of vectors `x` and `y`.
    """
    # Mean-center x -> mc_x
    mc_x = x - np.mean(x)
    # Mean-center y -> mc_y
    mc_y = y - np.mean(y)
    # a : Get sum of products of mc_x, mc_y
    a = mc_x.dot(mc_y)
    # b : Get sum of products of mc_x on mc_x
    b = mc_x.dot(mc_x)
    # c : Get sum of products of mc_y on mc_y
    c = mc_y.dot(mc_y)
    # return a / (sqrt(b) * sqrt(c))
    return a / (np.sqrt(b) * np.sqrt(c))



def pearson_2d(x, Y):
    """ Pearson product-moment correlation of vectors `x` and array `Y`

    Parameters
    ----------
    x : array shape (N,)
        One-dimensional array to correlate with every column of `Y`
    Y : array shape (N, P)
        2D array where we correlate each column of `Y` with `x`.

    Returns
    -------
    r_xy : array shape (P,)
        Pearson product-moment correlation of vectors `x` and the columns of
        `Y`, with one correlation value for every column of `Y`.
    """
    # Mean-center x -> mc_x
    mc_x = x - np.mean(x)
    # Mean-center every column of Y -> mc_Y
    mean_Y = np.mean(Y, axis=0)
    mean_Y_expanded = np.tile(mean_Y, (len(x), 1))
    mc_Y = Y - mean_Y_expanded
    # (Hint: np.tile, or (advanced, not yet covered) numpy broadcasting)
    # a : Get sum of products of mc_x and every column of mc_Y
    a = mc_x.dot(mc_Y)
    # b : Get sum of products of mc_x on mc_x
    b = mc_x.dot(mc_x)
    # c : Get sum of products of every column of mc_Y[:, i] on itself
    c = np.sum(mc_Y ** 2, axis=0)
    # return a / (sqrt(b) * sqrt(c))
    return a / (np.sqrt(b) * np.sqrt(c))
