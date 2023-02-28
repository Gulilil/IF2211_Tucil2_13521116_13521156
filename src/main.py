from in_out import *
from calculate import *
from bf import *
from dnc import *
from visualize import *

# Contains main algorithm
# Ask User Input
displayTitle("User Input")
data = validateUserInput()
print()

pointsArray = []
displayTitle("Generating Number")
for i in range(data[0]):
    pointsArray.append(generateNumber(data[1], data[2]))
print("Random points are successfully generated.")
print()

#Calculating (Divide and Conquer Algorithm)
displayTitle("Divide and Conquer Algorithm")

dncStart = startTime()

dncSolution = getSolutionDnC(pointsArray, data[0])

dncStop = stopTime()

print("Divide and Conquer Algorithm Execution Time : ", dncStop - dncStart)

print("The amount of solution: ", len(dncSolution))
print("The points that are considered as the closest pair(s) will be displayed below: ")
displayArr(dncSolution)
print()

print("The measured distance will be displayed below: ")
for i in range(len(dncSolution)):
    print((i+1), end=". ")
    print(getDistance(dncSolution[i][0], dncSolution[i][1]))
print()

#Calculating (Brute Force Algorithm)
displayTitle("Brute Force Algorithm")

bfStart = startTime()

bfSolution = getSolutionBF(pointsArray)

bfStop = stopTime()

print("Brute Force Algorithm Execution Time : ", bfStop - bfStart)

print("The amount of solution: ", len(bfSolution))
print("The index of the closest pair solution will be displayed below: ")
displayArr(bfSolution)
print()

print("The points that are considered as the closest pair(s) will be displayed below: ")
displayPointByIndex(pointsArray, bfSolution)
print()

print("The measured distance will be displayed below: ")
for i in range(len(bfSolution)):
    print((i+1), end=". ")
    print(getDistance(pointsArray[bfSolution[i][0]], 
                    pointsArray[bfSolution[i][1]]))
print()



#visualizing if the dots are in 3D
displayTitle("Visualizing")
if (data[1] == 3 or data[1] == 2): 
    print("Do you want to visualize the dots? (y/n)")
    answer = input(">> ")
    if (answer == "y"):
        visualize(pointsArray, dncSolution, data[0], data[1], data[2])
    else :
        print("The program has been stopped.")
else :
    print("It cannot be visualized.")

    