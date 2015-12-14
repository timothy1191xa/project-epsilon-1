""" Linear Regression on Begavioral data """

import sys
sys.path.append(".././utils")
from linear_regression import *

# Get the data
all_subjects= ['001', '002' ,'003', '004', '005', '006', '007', '008', '009', '010', '011', '012', '013', '014', '015', '016']
# data_dir = "/Users/macbookpro/Desktop/stat159_Project/"
project_path = '../../../'
data_dir = project_path+'data/'


########################
# combine all the data #
########################


all_data = []

# Loop for 16 subjects to get the data
for i in all_subjects:
	temp = load_data(i, data_dir)
	# if there's no such dataset, then stop running the loop and return nothing
	if temp is None:
		return
	all_data.append(temp)

# Concat the data
all_data = pd.concat(all_data)

# Calculate the difference for future use
all_data['diff'] = all_data['gain'] - all_data['loss']

# Calculate the ratio and other variables for future use
all_data['ratio'] = all_data['gain'] / all_data['loss']
all_data['log_gain'] = np.log(all_data['gain'])
all_data['log_loss'] = np.log(all_data['loss'])
all_data['log_diff'] = np.log(all_data['diff'])
all_data['log_ratio'] = np.log(all_data['ratio'])

# # Remove the rows that have respcat == -1 
#(meaning that the individual chooses to not participate the activity)
all_data = all_data[np.logical_not(all_data['respcat'] == -1)]


########################
#  Load each subject   #
########################

data_each = []

for i in all_subjects:
	data_each.append(load_data(i, data_dir))

for i in range(len(all_subjects)):
	data_each[i]['ratio'] = data_each[i]['gain'] / data_each[i]['loss']



##############################
#  Peform linear regression  #
##############################

data = all_data

# Run the linear_regression function to get the summary
linear_regression(data, 'RT', 'gain', 'loss')

linear_regression(data, 'RT', 'ratio')

linear_regression(data, 'RT', 'diff')


#######################
#        Plot         #
#######################



