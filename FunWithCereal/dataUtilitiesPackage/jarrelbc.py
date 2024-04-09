#jarrelbc.py

#The module should contain a function that returns a string with an interesting and gramatically correct sentence about the cereal data. 
# sentence will say the total number of calories for Apple_Jacks
from csvUtilitiesPackage.csvUtilities import readCSV

def jarrelbc():
       
    """
       Prints the sugar content of Apple Jacks cereal.
       Reads the cereal data from a CSV file and searches for the entry corresponding to
       Apple Jacks. Once found, it extracts and prints the sugar content of
       Apple Jacks.
       Returns: None
    """
    # Read the cereal data from the CSV file
    with open('..\dataPackage\\cereals.txt',"r") as file:
        lines = file.readlines()
           
    # Search for the line containing "Apple_Jacks"
        for line in lines:
            if "Apple_Jacks" in line:
                # Split the line by tab to
                #extract the fields
                fields = line.strip().split("\t")
                # Extract the sugar amount
                sugars = fields[9]
                # Print the sugar amount
                
                return f"The amount sugar in the Apple Jacks cereal is {sugars} grams. "
            