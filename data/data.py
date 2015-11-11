from __future__ import print_function, division

import hashlib
import os



def create_dict(filename):
    newDict={}
    f=open(filename)
    num_lines = sum(1 for line in open(filename))
    for line,i in zip(f,range(0,num_lines)):
        info = line.split()
        newDict[info[1]]=info[0]
    return newDict

def generate_file_md5(filename, blocksize=2**20):
    m = hashlib.md5()
    f= open(filename)
    while True:
        buf = f.read(blocksize)
        if not buf:
            break
        m.update(buf)
    return m.hexdigest()


def check_hashes(newDict):
    all_good = True
    for k, v in newDict.items():
        digest = generate_file_md5(k)
        if v == digest:
            print("The file {0} has the correct hash.".format(k))
        else:
            print("ERROR: The file {0} has the WRONG hash!".format(k))
            all_good = False
    return all_good

if __name__=="__main__":
    newDict = create_dict('ds005_raw_checksums.txt')
    print(check_hashes(newDict))
