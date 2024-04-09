# Ryan Wilkins
# wilkinrs@mail.uc.edu
# Assignment 10
# 4/9/2024
# IS4010-002
# Spring 2024
# Perform proper eclipse code structures and different types of data structures. As a team we had to all fork from the same repo and then push code so that all out 6+2 contribute to the same assignment. 
# Teaching ourselves how to work as a team and contribute to the same project. 
# Citations: Bill Nicholson
# Anything else that's relevant: NO

from csvUtilitiesPackage.csvUtilities import *
from pickle import NONE
myCereal = readCSV()


def wilkinrs(csv_file=r'..\dataPackage\cereals.txt'):
    '''
    Input: none 
    Return: A sentence about the calories per cup in Cinnamon Toast Crunch
    '''
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        
        for _ in range(76):
            next(reader, None)
            
        line_77 = next(reader, None)
        
        if line_77: 
            first_word_line_77 = line_77[0].split()[0]
            answer = f"{first_word_line_77}, is the breakfast of champions!"
            
    
        return answer
    
 