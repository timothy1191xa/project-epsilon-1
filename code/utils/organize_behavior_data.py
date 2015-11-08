import numpy as np

project_location="../../"
data_location=project_location+"data/ds005/"

"""subject 1"""

behav1=np.loadtxt(data_location+'sub001/behav/task001_run001/behavdata.txt',skiprows=1)
behav2=np.loadtxt(data_location+'sub001/behav/task001_run001/behavdata.txt',skiprows=1)
behav3=np.loadtxt(data_location+'sub001/behav/task001_run001/behavdata.txt',skiprows=1)


"""concatenate them to be 1"""
behav_total_run=np.concatenate((behav1,behav2,behav3),axis=0)

"""delete the rows that contain -1 in respcat (these are errors in experiment so we should take them out"""
behavior=np.delete(behav_total_run, np.where(behav_total_run[:,5]==-1),axis=0)

print(your "behavior" is ready to use!)