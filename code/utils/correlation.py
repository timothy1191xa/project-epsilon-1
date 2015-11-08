import numpy as np


"""get respcat only"""
respcat=behav[:,5]
"""-1 if respcat is 0"""
np.place(respcat, respcat==0, -1)

"""get respnum only"""
respnum=behav[:,4]

"""apply the weight"""
weighted_respcat=np.multiply(respcat, respnum)

"""get loss only"""
loss=behav[:,2]

"""get gain only"""
gain=behav[:,1]

"""check the correlation between loss and weighted_respcat"""

print("subject 1")
print(np.corrcoef(loss, weighted_respcat))

"""check the correlation between gain and weighted_respcat"""
print(np.corrcoef(gain, weighted_respcat))

"""Subject 1 is more responsive to gain"""



