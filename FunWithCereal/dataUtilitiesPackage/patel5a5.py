#patel5a5 
# Name:Akash Patel
# email:patel5a5@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/2024
# Course/Section:IS4010
# Semester/Year:Spring/2024
# Brief Description of the assignment:We are extracting cereal data 
# Brief Description of what this module does
# Citations:
# Anything else that's relevant:
from csvUtilitiesPackage.csvUtilities import *
def patel5a5():
    '''
    This functions demonstrates filtering data rows
    @return a print satment about a protien for a given cereals 
    '''
    myCereals = readCSV()
    myCereals = myCereals[10:11]
    cereals_name = [item[0] for item in myCereals]
    protien = [item[5] for item in myCereals]
    return f"{cereals_name} has {protien} grams of protien"
if __name__ == "__main__":
    print(patel5a5()) 
   
    
    
 
    