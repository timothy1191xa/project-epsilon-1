import pandas as pd
import numpy as np

#summary statistics for behavioral data (behavior.txt)

project_location="../../"
data_location=project_location+"data/ds005/"


def summary_file(run):
	fobj = open('summary_stats.txt', 'wt')
	a=run.describe()
	fobj.write(str(a))
	fobj.close()
	print(run.describe())

	return