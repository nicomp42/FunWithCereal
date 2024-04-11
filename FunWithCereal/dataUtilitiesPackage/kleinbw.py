#kleinbw
#The kleinbw function is defined here
# Ben Klein
# kleinbw@mail.uc.edu
# IS4010 Spring 2024

from csvUtilitiesPackage.csvUtilities import *
myCereals = readCSV()

def kleinbw():
    '''
    Input - None
    Return - Returns a print statement about the amount of calories for Apple_Cinnamon_Cheerios
    '''
    CeralRow = myCereals[5:6]
    calories = [item[3] for item in CeralRow]
    CerealName = [item[0] for item in CeralRow]
    return f".{CerealName} has {calories} calories"

#if __name__ == "__main__":
    #print(kleinbw())
    