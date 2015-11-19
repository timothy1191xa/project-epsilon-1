""" Linear Regression on Begavioral data """

import sys
sys.path.append(".././utils")
from linear_regression import *



data = combine_all_data()

linear_regression(data)

