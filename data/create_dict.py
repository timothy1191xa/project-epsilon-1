import 

def create_dict(
for line in f:
        listedline = line.strip().split('=') # split around the = sign
            if len(listedline) > 1: # we have the = sign in there
                        newDict[listedline[0]] = listedline[1]
