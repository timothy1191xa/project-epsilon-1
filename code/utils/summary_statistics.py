import pandas as pd
import numpy as np

#summary statistics for behavioral data (behavior.txt)

project_location="../../"
data_location=project_location+"data/ds005/"


def summary_file(run, subject_num):
	fobj = open('summary_stats.txt', 'wt')
	fobj.write("subject number : "+subject_num + '\n')
	a=run.describe()
	fobj.write(str(a))
	fobj.close()
	print("subject number 3 (total runs):" +'\n')
	print(run.describe())

	return