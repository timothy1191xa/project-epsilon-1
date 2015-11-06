import numpy as np

"""subject 1"""

behav1=np.loadtxt('ds005/sub004/behav/task001_run001/behavdata.txt',skiprows=1)
behav2=np.loadtxt('ds005/sub004/behav/task001_run002/behavdata.txt',skiprows=1)
behav3=np.loadtxt('ds005/sub004/behav/task001_run003/behavdata.txt',skiprows=1)



"""concatenate them"""
behav=np.concatenate((behav1,behav2,behav3),axis=0)

"""delete -1 """
behav=np.delete(behav, behav[:,5]==-1,axis=0)


"""get respcat only"""
respcat=behav[:,5]
#"""-1 if respcat is 0"""
#np.place(respcat, respcat==0, -1)

"""get respnum only"""
respnum=behav[:,4]

"""apply the weight"""
weighted_respcat=np.multiply(respcat, respnum)

"""get loss only"""
loss=behav[:,2]

"""get gain only"""
gain=behav[:,1]

"""check the correlation between loss and weighted_respcat"""
print(np.corrcoef(loss, weighted_respcat))

"""check the correlation between gain and weighted_respcat"""
print(np.corrcoef(gain, weighted_respcat))

"""Subject 1 is more responsive to gain"""



