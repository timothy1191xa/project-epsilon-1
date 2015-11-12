% Project Epsilon Progress Report
% Min Gu Jo, Kaam Soazig, Timothy Yu, Ye Zhi, Zhuangdi Li
% November 12, 2015

# Background

The Neural Basis of Loss Aversion in Decision-Making Under Risk


## The Paper

- from OpenFMRI.org
- https://www.openfmri.org/dataset/ds000005


## The Data

- 16 subjects
- multiple conditions per subject



## The Method

- linear regression

# Initial work

## EDA

- downloaded data
- simple plots, summary statistics

# Next steps

## Preprocessing / Validation

- PCA

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


