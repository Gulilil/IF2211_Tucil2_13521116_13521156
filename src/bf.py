from calculate import *


# ===================================================
# Calculation for Brute Force Algorithm
def getSolutionBF(arr):
    arrSolution = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            # Define the first pair of elements as the min tuple
            if (i == 0 and j == 1):
                # Min tuple will store the index of the shortest pair
                minTuple = (i, j)
                arrSolution.append(minTuple)
            else :
                if (getDistance(arr[i], arr[j]) < getDistance(arr[minTuple[0]], arr[minTuple[1]])):
                    arrSolution.clear()
                    minTuple = (i, j)
                    arrSolution.append(minTuple)
                elif (getDistance(arr[i], arr[j]) == getDistance(arr[minTuple[0]], arr[minTuple[1]])):
                    minTuple = (i,j)
                    arrSolution.append(minTuple)
    return arrSolution