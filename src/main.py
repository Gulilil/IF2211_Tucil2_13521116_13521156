from in_out import *
from calculate import *

# Contains main algorithm

# Ask User Input
displayTitle("User Input")
data = validateUserInput()
print()

# Generating Random Number
pointsArray = []
displayTitle("Generating Number")
for i in range(data[0]):
    pointsArray.append(generateNumber(data[1], data[2]))
print("Random points are successfully generated.")
print()

#Calculating (Divide and Conquer Algorithm)
displayTitle("Divide and Conquer Algorithm")

dncStart = startTime()

# Insert the algorithm here

dncStop = stopTime()

print("Divide and Conquer Algorithm Execution Time : ", dncStop - dncStart)
print()

#Calculating (Brute Force Algorithm)
displayTitle("Brute Force Algorithm")

bfStart = startTime()

bfSolution = getSolutionBF(pointsArray);

bfStop = stopTime()

print("The amount of solution: ", len(bfSolution));
print("The index list of the solution will be displayed below: ")
displayArr(bfSolution);

print("The measured distance will be displayed below: ")
for i in range(len(bfSolution)):
    print((i+1), end=". ")
    print(getDistance(pointsArray[bfSolution[i][0]], 
                    pointsArray[bfSolution[i][1]]))


print("Brute Force Algorithm Execution Time : ", bfStop - bfStart)

