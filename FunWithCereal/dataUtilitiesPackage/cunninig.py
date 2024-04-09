# Name: Ian Cunningham
# email:cunninig@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/2024
# Course/Section: App Dev
# Semester/Year: 2024
# Brief Description of the assignment: This is assignment 10
# Citations: Class and CHAT GPT

from csvUtilitiesPackage.csvUtilities import readCSV

def cunninig():
    """
    Prints the calorie content of Cinnamon Toast Crunch cereal.

    Reads the cereal data from a CSV file and searches for the entry corresponding to
    Cinnamon Toast Crunch. Once found, it extracts and prints the calorie content of
    Cinnamon Toast Crunch.

    Returns:
        None
    """
    # Read the cereal data from the CSV file
    with open('..\dataPackage\\cereals.txt', "r") as file:
        lines = file.readlines()
        
        # Search for the line containing "Cinnamon_Toast_Crunch"
        for line in lines:
            if "Cinnamon_Toast_Crunch" in line:
                # Split the line by tab to extract the fields
                fields = line.strip().split("\t")
                # Extract the calories
                calories = fields[3]
                # Print the calories
                print("There are a ton of calories in Cinnamon Toast Crunch. In this cereal, there are", calories,".")
                break  # Stop searching after finding the relevant line
    
if __name__ == "__main__":
    # Test code
    cunninig()