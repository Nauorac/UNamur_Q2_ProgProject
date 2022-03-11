
import os

def data_import():
    # Ask for ano file path
    path = input("Please give the path to the .ano file : ")
    # Tuple for map size
    size = ()
    # A unique dictionnary to rules them all
    entities = {}
    # Open .ano file
    with open(path, "r+") as file:
        # Read the entire file and store it into a list.
        brut = file.readlines()
        for i in brut:
            # Ignore string line
            if (i[0] == "m") or (i[0] == "w") or (i[0] == "f"):
                continue
            # Detect if line contains boardgame size
            if len(i) <= 6:
                si = i.split()
                size = (int(si[0]), int(si[1]))
                continue
            j = i.split()
            # Check if line contain werewolf info or not
            if (j[3] == "alpha") or (j[3] == "omega") or (j[3] == "normal"):
                x = int(j[1])
                y = int(j[2])
                values = [int(j[0]), (j[3]), 100]
                entities.update({(x, y): values})
            else:
                x = int(j[0])
                y = int(j[1])
                # Add "0" as first list value element for food to make the "food team" identified with 0
                values = [0, (j[2]), int((j[3]))]
                entities.update({(x, y): values})
    print("Map Size : ", size)
    print("Entities :", entities)


data_import()
#C:\Users\Seb\Documents\GitHub\UNamur_Q2_ProgProject\_3_Dossier de travail\_00_Global\example.ano

"""
file = input("Enter the Filename: ")
extension = file.split(".")
print ("The extension is: " + (extension[-1]))
"""