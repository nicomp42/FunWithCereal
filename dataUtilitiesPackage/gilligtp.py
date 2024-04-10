#gilligtp.py
'''
# Name: Tom Gilligan
# email: gilligtp@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/24
# Course/Section: 002
# Semester/Year: Spring 24
# Brief Description of the assignment: read csv data and push
# Citations: w3schools, the google, stackoverflow
# Anything else that's relevant: n/a
'''
import csv

def gilligtp():
    
    
    """
    Finds and prints information about the cereal with the most fiber per gram.
    @return: fiberiest_cereal
    """

    max_fiber = 0
    fiberiest_cereal = None

    with open('..\dataPackage\\cereals.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        next(csv_reader)  # Skip the header row 

        for row in csv_reader:
            cereal_name = row[0]
            fiber = float(row[10])

            if fiber > max_fiber:
                max_fiber = fiber
                fiberiest_cereal = cereal_name

    if fiberiest_cereal:
        print(f"This cereal has the most fiber per gram: {fiberiest_cereal}") 

gilligtp()
