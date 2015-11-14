% Project Epsilon progress presentation
% Min Gu Jo, Soazig Kaam, Zhuangdi Li, Timothy Yu, Ye Zhi
% November 12, 2015


# Background


## The Paper

- The Neural Basis of Loss Aversion in Decision-Making Under Risk
- from OpenFMRI.org
- https://www.openfmri.org/dataset/ds000005
- ds005

## The Study

- 16 subjects were presented gambling situations with 50% chance of winning
- Each of the 255 trials was associated with amounts of potential gains and losses (in $)
- Subjects ranked their level of willingness to accept or reject the gamble on 4 point likert scale
	1. Strongly accept    
	2. Weakly accept      
	3. Weakly reject     
	4. Strongly reject    


# Our Progress

## Initial work

- Downloaded data and used the checksums.txt to validate
- Behavior data: merged three runs for each subject and took out observations with -1 in “respcat”(maybe an error in the experiment)
- Bold data: unzip all files 


## Behavior data (1/3)

- Simple plots and summary statistics for each subject

![](pictures/statsdata-Min_20151112_V2.png)

## Behavior data (2/3)

- Logistic regression between Response(1/0 or Accept/Reject) and Gain/Loss
	*Scientific Question: If gain/loss would be significant for whether individuals would like to participate in the gamble
	*Result: According to our analysis, the decision to whether take the gamble of most of subjects, in general, is more affected by loss amount rather than by gain amount.
![](pictures/log_regression-Min_20151112.png)

## Behavior data (2/3)

- Linear Regression between Response time and Gain/Loss/Ratio
	*Result: Ratio is a significant predictor and people would actually care more about loss than gain 

![](pictures/linear_regression-Tim_20151112.png)


## BOLD data

- Reproduced Quality Assurance Plots: mean, fd and dvars
- Calculated the correlation between task-on/task-off vectors and voxel time courses to identify the active region of the brain

![](pictures/correlations.png)

- Tried to use brain image data(mean/sd across time courses) to identify gain/loss ratio, choices(accept/reject) and (strongly/weekly accept/reject)


# Our research plan

## Behavior data

- Use other classification methods than logistic regression to predict gamble/not gamble
- Explore correlation between neural activity (image data) and behavior data (survey data)
	- Can we use the image to predict behavior data ?

## Modeling voxels for each participant

- Use convolved hemodynamic response and linear regression 
- Train of the model using two randomly selected runs 
- Validating the model using the third run 
- Investigate different Gamma function shape parameters 

## BOLD images data analysis

- Identify brain activation region associated with decision making 
	- Use K-means or other classification  
	- Assess the sensitivity to gail and loss
- Compare across subject and runs (for now, only for 1 subject and 1 run)

## Model validation

- Check assumptions of the regression models: normality, independance, equal variance
- Use cross validations to test our model accuracy


# The problems we’ve faced

## Understand the data

- Lack documentation of the data structure and meaning of variables:
	- spend much time reading through the paper and searching the website
	- still some problems unsolved: 
		e.g. PTval in the behavior data of each run of each subject

- fMRI: technical field study difficult to understand
- Insufficient description of the analysis methods used to reproduce the work
	- e.g. QA section we can not match the scale/value of some variables
	- e.g. analysis of the individual logistic regressions for behavioral data

## Coding

- Reproducibility:
	- For purpose of reproducible, we need to write a lot of functions, scripts and tests to travel through different folders, unzip and load the files
	-- checksum.txt   match hash and files

- Git:
	- Doing version control; merge results; branch management
	- Keep track of others’ code
		--  solved by adding more descriptions when making pull request 
		--  review

## Data Analysis

- Image data analysis
	- Difficulties when working on data across subjects and runs

- Length of behavior data does not match the length of image data
	- Fill in 0 or NA?

- Convolution
	-  How to create a convolution matrix
	-  Can not determine the parameters of the gamma distribution
		- Using the common 2 Gamma functions (shape parameter:6 and 12) not reasonable
		- Find other sources (literature review)

##  Inference from data: future attempt to validate your model

- Assumption check
	- Analysis of residuals
	- Normality
- p-values
- Validation using R2
- Cross-validation


# Our Process

## Challenges

- Understanding the paper and the fMRI data
- Workflow on git and version control management (some problem with branch management and Travis CI)
- Difficulty with code review process
- Conflicting schedules but manage to set up a weekly meeting
- Overcome the overwhelming amount of data/work by working in smaller groups

## Improving reproducibility 

- Adopt a systematic method for code organization (functions, script, test) and writing (PEP 0008)
- Improve our process of code review
- Generate the support documentation to improve usability of our project 
- Exchange more with groups working on the same topic


# Feedback on the class

## Feedback

- A good model with 3 (or 4) supervisors with their own expertise
- Would like more exposure to machine learning techniques (also the Basic linear model is one example)
- Lectures on git workflow and collaboration were very useful but fast-paced. 
- Lecture on linear algebra was a good refresher but fast-paced and too theoretical
- Would like more linear regressions course focusing on the implementation

## Ideas for improvement

<<<<<<< HEAD
## Our research plan
- Modeling voxels with convolved hemodynamic response and linear regression for each participant
- Investigate for more suited shape parameters for the Gamma function primarily with literature review
- for BOLD image data analysis, we might need to compare across subject and runs. For now, I only did for one person one run.
-check the assumptions of the regression models: normality, independence, equal variance

## Statistical Analysis

- linear model



# the problems we?ve faced

## understand the data

## Coding

## Data Analysis

# Our Process

## Challenges

- Understanding the paper and the fMRI data (could dissuade from extending the references list for the project)
- Workflow on git and version control management (some problem with branch management and Travis CI)
- Difficulty with code review process
- Conflicting schedules but manage to set up a weekly meeting
- Overcome the overwhelming amount of data/work by working in smaller groups

## Improving reproducibility 
- Adopt a systematic method for code organization (functions, script, test) and writing (PEP 0008)
- Improve our process of code review
- Generate the support documentation to improve usability of our project 
- Exchange more with groups working on the same topic

# Feedback on the class

## Feedback
- A good model with 3 (or 4) supervisors with their own expertise
- Would like more exposure to machine learning techniques (also the Basic linear model is one example)
- Lectures on git workflow and collaboration were very useful but fast-paced. 
- Lecture on linear algebra was a good refresher but fast-paced and too theoretical
- Would like more linear regressions course focusing on the implementation

## Idea of improvement
- Supporting the lecture with slides or handouts with the fundamentals (e.g. git command for collaborative work) we can refer to after class
- Provide a support document with the mostly used statistics definitions for a good analysis design and interpretation


=======
- Supporting the lecture with slides or handouts with the fundamentals (e.g. git command for collaborative work) we can refer to after class
- Provide a support document with the mostly used statistics definitions for a good analysis design and interpretation

>>>>>>> upstream/master
