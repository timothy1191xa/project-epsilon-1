# project-template
[![Build Status](https://travis-ci.org/berkeley-stat159/project-epsilon.svg?branch=master)](https://travis-ci.org/berkeley-stat159/project-epsilon?branch=master)
[![Coverage Status](https://coveralls.io/repos/berkeley-stat159/project-epsilon/badge.svg?branch=master)](https://coveralls.io/r/berkeley-stat159/project-epsilon?branch=master)

# Project Epsilon
## UC Berkeley's Statistics 159/259
### Project Group Epsilon, Fall Term 2015 

_**Topic:**_ [The Neural Basis of Loss Aversion in Decision-Making Under Risk] 

### Navigation
 - Data `make download_data` : Downloads the ds005 dataset including brain scan 
 images of total 16 subjects. Be aware of the size of the data ~ 3GB.
 
 - Filtered data `make download_filtered_data` : Download the filtered data
   provided by the Montreal Neurogical Institute relative to this study as well
   as the mask function and template for the visualization. There size of the 
   data is 14GB.
  
 - Data `make download_all` : Will download the raw and filtered data 
   mentionned above as well as data from the ds114 project used to test 
   our functions. The total size of the file is ~17GB.
 
 - Data `make download_test_data` : Will download 3 files from the ds114 project 
   used to test our functions..

 - Validate `make validate_data` : Validates the downloaded data (only applied
   on ds005 data)

 - Test `make test` : Tests the functions in tests folder with nosestests

 - Coverage `make coverage` : Creates a coverage report for data

 - Verbose `make verbose` : Tests the functions in tests folder via nosetests 
   and comments

