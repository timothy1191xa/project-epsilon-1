"""
Creates a .json file with hashes for our ds005 data from text file
containing file names and corresponding hashes.
"""
from __future__ import print_function
from manage_hashes import create_dict 
import json
import pdb

if __name__=="__main__":
#For our data ds005
    newDict = create_dict('ds005_raw_checksums.txt')
    with open('ds005_hashes.json', 'w') as file_out:
        json.dump(newDict, file_out)
#    print(check_hashes(newDict))
