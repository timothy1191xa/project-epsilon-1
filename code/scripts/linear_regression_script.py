""" Linear Regression on Begavioral data """

import sys
sys.path.append(".././utils")
from linear_regression import *

# Get the data
data = combine_all_data()

# Run the linear_regression function to get the summary
beta_gain_and_loss, p_gain_and_loss = linear_regression(data, 'RT', 'gain', 'loss')

beta_ratio, p_ratio = linear_regression(data, 'RT', 'ratio')

beta_diff, p_diff = linear_regression(data, 'RT', 'diff')
