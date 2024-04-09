# main.py
# Entry point for the project is defined here.
# Bill Nicholson
# nicholdw@ucmail.uc.edu
# IS4010 Spring 2024

from csvUtilitiesPackage.csvUtilities import *

if __name__ == "__main__":

    students = ["cunninig", "gilligtp", "harrints", "jarrelbc"
              , "kleinbw", "lisowsmd", "moorehc", "patel5a5"
              , "shahh4", "stapleet", "troegele", "wilkinrs"
              , "willi6d3", "wogomomr"]
    for student in students:
        try:
            # Build the import statement in a string and execute it
            cmd = "from dataUtilitiesPackage." + student + " import " + student
            exec(cmd)
        except Exception as e:
            print(e) 
            print("cmd:", cmd)
            print("**** Import failed for " + student + "*****")

    myCereals = readCSV()
    print(myCereals)

    for student in students:
        try:
            # Build the code in a string and execute it 
            exec("print(" + student + "())")
        except Exception as e:
            print(e) 
            print("**** Code execution failed for " + student + "*****")
