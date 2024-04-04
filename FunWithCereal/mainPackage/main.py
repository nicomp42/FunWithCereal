# main.py
# Entry point for the project is defined here.
# Bill Nicholson
# nicholdw@ucmail.uc.edu
# IS4010 Spring 2024

from csvUtilitiesPackage.csvUtilities import *

try:
    from dataPackage.cinninig import cunninig
except:
    pass

if __name__ == "__main__":

    myCereals = readCSV()
    print(myCereals)
    
    try:
        cunninig()
    except:
        pass
    