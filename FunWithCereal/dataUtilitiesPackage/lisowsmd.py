# lisowsmd.py
# Name: Matthew Lisowsky
# email: lisowsmd@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: In this module we look at the information for cinnamon toast crunch
# Citations: https://chat.openai.com/
# Anything else that's relevant:

# imports (ex: from functionPackage.functions import *)
from csvUtilitiesPackage.csvUtilities import readCSV

def lisowsmd():
    '''
    The sentence pulls the amount of sugar in CTC
    @parameter: none
    @return: amount of sugar
    '''
    cereals_data = readCSV()
    
    for row in cereals_data:
        if "Cinnamon_Toast_Crunch" in row:
            sugar = row[10]  # Assuming sugar is at index 10
            print("Cinnamon Toast Crunch has", sugar, "grams of sugar.")
            break  # Stop searching after finding the relevant line
        
if __name__ == "__main__":
    lisowsmd()