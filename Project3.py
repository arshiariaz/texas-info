# File: Project3.py
# Student: Arshia Riaz
# UT EID: ar65892
# Course Name: CS303E
# 
# Date Created: 11/21/2021
# Date Last Modified: 12/01/2021
# Description of Program: This program provides information pertaining to the populations of Texas counties and statewide.

def read_file(filename):
    file = open(filename, 'r')
    
    rec = {}
    countiesnames = []
    
    sumcensus2010 = 0
    sumestimated2020 = 0
    
    for line in file:
        if not line.startswith('#'):
            countyName, census2010, estimated2020 = [i.strip() for i in line.split(',')]
            
            census2010 = int(census2010)
            estimated2020 = int(estimated2020)
            
            rec[countyName.title()] = (census2010,estimated2020)
            
            sumcensus2010 += census2010
            sumestimated2020 += estimated2020
            
            countiesnames.append(countyName.title())
    
    rec['Texas'] = (sumcensus2010,sumestimated2020)
    
    return rec, countiesnames

from os import path
filename = 'populationdata.csv'

if not path.isfile(filename):
    print("File populationdata.csv not found.")
    exit()

rec, countiesnames = read_file(filename)

print("Welcome to the Texas Population Dashboard.")
print("This provides census data from the 2010 census and")
print("estimated population data in Texas as of 1/1/2020.")
print()
print("Creating dictionary from file: populationdata.csv")
print()
print("Enter any of the following commands:")
print("Help - list available commands;")
print("Quit - exit this dashboard;")
print("Counties - list all Texas counties;")
print("Census <countyName>/Texas - population in 2010 census by specified county or statewide;")
print("Estimated <countyName>/Texas - estimated population in 2020 by specified county or statewide.")
print("Growth <countyName>/Texas - percent change from 2010 to 2020, by county or statewide.")
print()

while True:
    commandInput = input("Please enter a command: ")
    commWords = commandInput.split()
    comm = commWords[0].strip()

    args = commWords[1:]
    arg = " ".join(args).strip()
    
    if comm.lower() == 'help':
        print("Help - list available commands;")
        print("Quit - exit this dashboard;")
        print("Counties - list all Texas counties;")
        print("Census <countyName>/Texas - population in 2010 census by specified county or statewide;")
        print("Estimated <countyName>/Texas - estimated population in 2020 by specified county or statewide.")
        print("Growth <countyName>/Texas - percent change from 2010 to 2020, by county or statewide.")
        print()

    elif comm.lower() == 'quit':
        print("Thank you for using the Texas Population Database Dashboard.  Goodbye!")
        exit()
        
    elif comm.lower() == 'counties':
        print(", ".join([j if i % 10 != 0 else '\n'+j for i, j in enumerate(countiesnames)]).strip(), end="\n\n")
                
    elif comm.lower() == 'census':
        if arg.lower() == 'texas':
            print("Texas total population in the 2010 Census:", rec['Texas'][0], end="\n\n")
            
        elif arg.title() in countiesnames:
            print("{} county had {} citizens in the 2010 Census.".format(arg.title(), rec[arg.title()][0]), end="\n\n")
            
        else:
            print("County {} is not recognized.".format(arg.title()), end="\n\n")
    
    elif comm.lower() == 'estimated':
        if arg.lower() == 'texas':
            print("Texas estimated population (January, 2020):", rec['Texas'][1], end="\n\n")
            
        elif arg.title() in countiesnames:
            print("{} county had estimated population (January, 2020): {}".format(arg.title(), rec[arg.title()][1]), end="\n\n")
            
        else:
            print("County {} is not recognized.".format(arg.title()), end="\n\n")
            
    elif comm.lower() == 'growth':
        if arg.lower() == 'texas':
            growthcalc = ((int(rec['Texas'][1])-int(rec['Texas'][0]))/int(rec['Texas'][0]))*100
            print("Texas had percent population change (2010 to 2020): ", format(growthcalc,'.2f'),"%", sep='',end="\n\n")
            
        if arg.title() in countiesnames:
            growthcalc = ((int(rec[arg.title()][1])-int(rec[arg.title()][0]))/int(rec[arg.title()][0]))*100
            print("{} county had percent population change (2010 to 2020): {}%".format(arg.title(), format(growthcalc,'.2f')), end="\n\n")
        
    
    else:
        print("Command is not recognized.  Try again!", end="\n\n")
