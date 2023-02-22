from in_out import *
from calculate import *

# Contains main algorithm

# Ask User Input
displayTitle("User Input")
data = validateUserInput()

# Generating Random Number
pointsArray = []
displayTitle("Generating Number")
for i in range(data[0]):
    pointsArray.append(generateNumber(data[1], data[2]))
print("Random points are successfully generated.")

#Calculating (Divide and Conquer Algorithm)
displayTitle("Divide and Conquer Algorithm")


#Calculating (Brute Force Algorithm)
displayTitle("Brute Force Algorithm")
