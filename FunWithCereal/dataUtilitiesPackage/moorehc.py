#moorehc.py
# Name: Harrison Moore
# email: Moorehc@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/2024
# Course/Section: Advanced App Dev 002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Fork and complete the FunWithCereal Project

# Brief Description of what this module does. Breakout assignment to create a function which returns a grammatically correct sentence about the cereal dataset.
# Citations: Chat GPT
# Anything else that's relevant:

from csvUtilitiesPackage.csvUtilities import readCSV #Import statement

def moorehc():
    try:
        # Call the readCSV function to get the data
        cereals_data = readCSV()
        
        # Count the number of cereals (excluding the header)
        num_cereals = len(cereals_data) - 1 if cereals_data else 0
        
        return f"There are {num_cereals} types of cereals in the dataset."
    except FileNotFoundError:
        return "Error: 'cereals.txt' file not found."

if __name__ == "__main__": #Entry point
    print(moorehc())
    
    
    
    