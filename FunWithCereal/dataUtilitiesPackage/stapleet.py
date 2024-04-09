# Name:Elizabeth Stapleton
# email: stapleet@mail.uc.edu
# Assignment Number: stapleet_Assignment10
# Due Date: 04/11/2023
# Course/Section: IS4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: Creating a function to take the provided csv file and extract a piece of interesting data from it.
# Citations:
# Anything else that's relevant:

from csvUtilitiesPackage.csvUtilities import readCSV


def stapleet():
    '''
    Analyzes the cereal data to find the amount of calories in the cereal.
    @param: None
    @return: Sentence about the extracted data.
    '''
    
    # Read the cereal data from the CSV file
    cereals = readCSV()
    
    if cereals is None:
        return "Error: unable to read cereal data."
    
    # Initialize variable to store calorie information
    cereal_calories = None
    cereal_name = 'Clusters'

    # Search for the specified cereal
    for cereal in cereals:
        if cereal[0].lower() == cereal_name.lower():
            cereal_calories = int(cereal[3])
            break

    # Return calorie information if found, otherwise return None
        # Return calorie information if found, otherwise return None
    if cereal_calories is not None:

        return print(f"The number of calories in {cereal_name} is {cereal_calories}.")
    else:
        return print(f"Sorry, the calories for {cereal_name} could not be found.")


if __name__ == "__main__":
    stapleet()  
