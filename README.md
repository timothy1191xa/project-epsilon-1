# project-template
[![Build Status](https://travis-ci.org/berkeley-stat159/project-epsilon.svg?branch=master)](https://travis-ci.org/berkeley-stat159/project-epsilon?branch=master)
[![Coverage Status](https://coveralls.io/repos/berkeley-stat159/project-epsilon/badge.svg?branch=master)](https://coveralls.io/r/berkeley-stat159/project-epsilon?branch=master)

# Project Epsilon
## UC Berkeley's Statistics 159/259
### Project Group Epsilon, Fall Term 2015 

_**Topic:**_ [The Neural Basis of Loss Aversion in Decision-Making Under Risk] 

## Overview
This repository attempts to reproduce the original analysis on "The Neural Basis of Loss Aversion in Decision-Making Under Risk" done by Sabrina M. Tom, Craig R. Fox, Christopher Trepel, Russell A. Poldrack. The imaging data were collected using the fMRI method. They were processed and analyzed in order to identify the regions of the brain activated by the decision making process. This study also investigated the relationship between the brain activity and the behavior of the subjects towards the gambling situations using a whole-brain robust regression analysis. 
Please follow the insturctions to explore on the repository.


## Directions
1. Clone the repo: `git clone https://github.com/berkeley-stat159/project-epsilon.git'
2. Install python dependencies with pip: `pip install -r requirements.txt` 

### Navigation
 - Data `make data` : Downloads the ds005 dataset including brain scan images of totl 16 subjects

 - Validate `make validate` : Validates the downloaded data to check if it's ok to run on 

 - All Analysis `make all-analysis` : Executes all analysis and creates relevant img files under fig/ folder

 - Test `make test` : Tests the functions in code/utils folder

 - Coverage `make coverage` : Creates a coverage report for the functions in code/utils/ folder

 - Verbose `make verbose` : Tests the functions in code/utils folder via nosetests option

 - Report `make verbose` : Creates a report in pdf file under paper/ folder

## Contributors
Min Gu Jo ([`mingujo`](https://github.com/mingujo))\\
Soazig Kaam ([`soazig`](https://github.com/soazig))\\
Zhuangdi Li ([`lizhua`](https://github.com/lizhua))\\
Ye Zhi ([`ye-zhi`](https://github.com/ye-zhi))\\
Timothy Yu ([`timothy1191xa`](https://github.com/timothy1191xa))\\
