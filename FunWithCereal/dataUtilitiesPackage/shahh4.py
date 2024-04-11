# shahh4.py 
# Name: Harsh Shah
# email: shahh4@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 04/11/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Return healthiest cereal from cereal data in cereal.txt file
# Anything else that's relevant: Used worked done in class as a reference as well as ChatGPT to solve errors. 

import csvUtilitiesPackage.csvUtilities as csvUtil

def calculate_score(row):
    """
    Calculate the score of a cereal row based on certain criteria. 
    @parameters: row (list): A list representing a row of cereal data.     
    @returns: float: The calculated score for the cereal row.
    """
    score = 0
    score += (140 - int(row[3])) / 140 * 100  # Lower calorie content is better   
    score += (int(row[4]) - 1) / 6 * 100  # Higher protein content is better   
    score += (3 - int(row[5])) / 3 * 10      # Lower fat content is better
    score += (15 - int(row[9])) / 15 * 100     # Lower sugar content is better
    return score

def shahh4():
    """
    @param: Read cereals.txt file and return a sentence showing the healthiest cereal from the text file data.
    @returns: str: A sentence indicating the healthiest cereal and its rating.
    """
    cereals = csvUtil.readCSV()  # Call the readCSV function from csvUtilities
    healthiest_cereal = max(cereals[1:], key=lambda row: calculate_score(row))
    sentence = f"The healthiest cereal is {healthiest_cereal[0]} with a rating of {healthiest_cereal[-1]}."
    return sentence

if __name__ == "__main__":
    print(shahh4())


