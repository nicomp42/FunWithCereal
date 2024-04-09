# Ryan Wilkins
# wilkinrs@mail.uc.edu
# Assignment 10
# 4/9/2024
# IS4010-002
# Spring 2024
# Perform proper eclipse code structures and different types of data structures. As a team we had to all fork from the same repo and then push code so that all out 6+2 contribute to the same assignment. 
# Teaching ourselves how to work as a team and contribute to the same project. 
# Citations: Bill Nicholson
# Anything else that's relevant: NO

from csvUtilitiesPackage.csvUtilities import *
myCereal = readCSV()


def wilkinrs():
    CT = myCereal[12:13]
    cal = [iteam[3]for iteam in CT]
    cup = [iteam[14] for iteam in CT]
    cerealName = [iteam[0] for iteam in CT]
    print("".join(cerealName),"contains", "".join(cal),"calories for every", "" .join(cup),"cups!")
