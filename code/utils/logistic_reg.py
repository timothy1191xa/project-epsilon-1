import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np

#PREDICT SUBJECT's DECISION TO WHETHER GAMBLE OR NOT GIVEN WITH GAIN AND LOSS AMOUNT using LOGISTIC REGRESSION

project_location="../../"
data_location=project_location+"data/ds005/"

run1 = pd.read_table(data_location+"sub001/behav/task001_run001/behavdata.txt")
run2 = pd.read_table(data_location+"sub001/behav/task001_run002/behavdata.txt")
run3 = pd.read_table(data_location+"sub001/behav/task001_run003/behavdata.txt")

run_1=run1.append(run2)
run_total=run_1.append(run3) #append all the data frames of run

a = run_total.drop('onset', 1) # drop onset column

run_organized = a.drop('PTval', 1) # drop PTval column

cols = run_organized.columns.tolist() # reorganize the columns
cols.insert(0, cols.pop(cols.index('respcat'))) # put respcat into front
run_organized = run_organized.reindex(columns= cols) # reorganize

run_final = run_organized.drop(run_organized[run_organized.respcat == -1].index) # drop error in experiment

train_cols = run_final.columns[1:3] # train columns are gain and loss
logit = sm.Logit(run_final['respcat'], run_final[train_cols]) # do regression
result = logit.fit()
result.summary()

run_final['respcat_pred']=result.predict(run_final[train_cols]) # add prediction on the data frame
