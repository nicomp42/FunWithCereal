# troegele.py
# Name: Leonie Troeger
# email: troegele@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 04/11/2024
# Course/Section: IS 4010 - 002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Team assignment that prints and returns protein value of Cinnemon Toast Crunch.
# Citations: 
# Anything else that's relevant:


from csvUtilitiesPackage.csvUtilities import readCSV
    
def troegele():
   """
   Prints the protein content of Cinnamon Toast Crunch cereal.
   Reads the cereal data from a CSV file and searches for the entry corresponding to
   Cinnamon Toast Crunch. Once found, it extracts and prints the protein content of
   Cinnamon Toast Crunch.
   Returns: None
   """
   # Read the cereal data from the CSV file
   with open('..\dataPackage\\cereals.txt',"r") as file:
       lines = file.readlines()
       
       # Search for the line containing "Cinnamon_Toast_Crunch"
       for line in lines:
        if "Cinnamon_Toast_Crunch" in line:
            # Split the line by tab to
            #extract the fields
            fields = line.strip().split("\t")
            # Extract the calories
            proteins = fields[4]
            # Print the calories
            #print("Cinnemon Toast Crunch has ", proteins," gramm of protein.")
            #break
            return f"Cinnemon Toast Crunch has {proteins} gramm of protein."
  # Stop searching after finding the relevant line
    
       return None   
   

     