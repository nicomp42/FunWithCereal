# csvUtilities
# Utility functions for processing the CSV files are defined here
# Bill Nicholson
# nicholdw@ucmail.uc.edu
# IS4010 Spring 2024
import csv


def readCSV():
    """
    Read the cereals CSV file into a list of lists
    @return: The list of lists
    """
    with open('..\dataPackage\\cereals.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        cereals = []
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                cereals.append(row)
                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        # print(cereals)
    return cereals
