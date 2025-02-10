#PartB.py
#10/02/2025
#b00152481

def printSteps(a, b):                    #Defines(def) a function(printsteps)that takes 2 parameters (a&b)
    for step in range(a, b + 1):         #A for loop that runs from a to b. +1 is needed because range() exludes last number.
        print (f"Step {step}")           #

printSteps(4, 6)

