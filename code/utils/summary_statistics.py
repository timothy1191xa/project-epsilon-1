

#summary statistics for behavioral data (behavior.txt)


import pandas as pd
import numpy as np

project_location="../../"
data_location=project_location+"data/ds005/"

run1 = pd.read_table(data_location+"sub001/behav/task001_run001/behavdata.txt")
run2 = pd.read_table(data_location+"sub001/behav/task001_run002/behavdata.txt")
run3 = pd.read_table(data_location+"sub001/behav/task001_run003/behavdata.txt")

run_1=run1.append(run2)
run=run_1.append(run3) #append all the data frames of run

print("run1")
print(run1.describe())
print("run2")
print(run2.describe())
print("run3")
print(run3.describe())

print("total run")
print(run.describe())

