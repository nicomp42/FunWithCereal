from csvUtilitiesPackage.csvUtilities import *

def willi6d3():
    '''
    
    '''
    myCereals = readCSV()
    myCereals = myCereals[9:10]
    cereals_name = [item[0] for item in myCereals]
    protein = [item[5] for item in myCereals]
    return f"{''.join(cereals_name)} has {''.join(protein)} grams of protein"

if __name__ == "__main__":
    willi6d3()
