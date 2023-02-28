from in_out import *
from calculate import *
from bf import *
from dnc import *
from visualize import *
from globalCounts import *

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

displaySubTitle("Euclidean Distance Counts")
print(getCountsDnC())
displaySubTitle("Execution Time")
print(dncStop - dncStart)
displaySubTitle("Amount of Solution")
print(len(dncSolution))
displaySubTitle("Nearest Distance")
print(getDistance(dncSolution[0][0], dncSolution[0][1]))
displaySubTitle("Points")
print()
displayPoints(dncSolution)
print()

#Calculating (Brute Force Algorithm)
displayTitle("Brute Force Algorithm")

bfStart = startTime()
bfSolution = getSolutionBF(pointsArray)
bfStop = stopTime()

displaySubTitle("Euclidean Distance Counts")
print(getCountsBF())
displaySubTitle("Execution Time")
print(bfStop - bfStart)
displaySubTitle("Amount of Solution")
print(len(bfSolution))
displaySubTitle("Nearest Distance")
print(getDistance(pointsArray[bfSolution[0][0]], pointsArray[bfSolution[0][1]]))
displaySubTitle("Points")
print()
displayPointByIndex(pointsArray, bfSolution)
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

    