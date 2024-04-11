# Name: Maddy Wogomon
# email: wogomomr@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Fun with cereal

# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this.
# Citations: https://chat.openai.com/c/4b10a524-9636-40a0-ab46-eb8044fc807f
# Anything else that's relevant:

import csv

def readCSV():
    """
    Read the cereals CSV file into a list of lists
    @return: The list of lists
    """
    with open(r'..\dataPackage\cereals.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        cereals = []
        for row in csv_reader:
            if line_count == 0:
                # Skip the header row
                line_count += 1
            else:
                cereals.append(row)
                line_count += 1
    return cereals

def wogomomr():
    data = readCSV()
    # Extracting the names of cereals with the highest ratings
    highest_rated_cereals = []
    max_rating = max(data, key=lambda x: float(x[-1]))[-1]
    for entry in data:
        if entry[-1] == max_rating:
            highest_rated_cereals.append(entry[0])

    # Forming the sentence
    if len(highest_rated_cereals) == 1:
        sentence = f"The highest rated cereal is '{highest_rated_cereals[0]}' with a rating of {max_rating}."
    else:
        cereals_str = ", ".join(f"'{cereal}'" for cereal in highest_rated_cereals[:-1])
        sentence = f"The highest rated cereals are {cereals_str}, and '{highest_rated_cereals[-1]}' with a rating of {max_rating}."

    return sentence

# Sample usage
print(wogomomr())

