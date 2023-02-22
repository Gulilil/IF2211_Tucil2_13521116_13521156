import random
import time
import numpy as py



# Random Number
def generateNumber(length, boundaries):
    # Generate random number (float) and inserting it into a tuple
    # Generated random number will be in range of (-boundaries < x < boundaries)
    container = []
    for i in range (length):
        container.append(random.uniform(-boundaries, boundaries))
    return tuple(container)

# Time
def startTime():
    return time.time()  

def stopTime():
    return time.time()

def convertToSeconds(micros):
    return micros* (10 ** 6)

# Distance calculation
def getDistance(arr1, arr2):
    # Determine the distance of two points
    res = 0
    for i in range(len(arr1)):
        res += (arr2[i] - arr1[i])**2
    return res**(0.5)

# ===================================================
# Contains calculation of Divide and Conquer Algorithm

# Data Sorting
def mergeArr(arr1, arr2, elmt):
    # Merging two sorted array
    new = [0 for i in range(len(arr1) + len(arr2))]
    idx1 = 0
    idx2 = 0
    idx = 0
    while (idx1 < len(arr1) or idx2 < len(arr2)):
        if (idx1 == len(arr1)):
            new[idx] = arr2[idx2]
            idx2 += 1
            idx += 1
        elif (idx2 == len(arr2)):
            new[idx] = arr1[idx1]
            idx1 += 1
            idx += 1
        else:
            if (arr1[idx1][elmt] < arr2[idx2][elmt]):
                new[idx] = arr1[idx1]
                idx1 += 1
                idx += 1
            else :
                new[idx] = arr2[idx2]
                idx2 += 1
                idx += 1
    return new

def splitArrBot(arr, n):
    new = []
    for i in range(n):
        new.append(arr[i])
    return new

def splitArrTop(arr, n):
    new = []
    for i in range (n, len(arr)):
        new.append(arr[i])
    return new

def mergeSort(arr, elmt):
    # Will be sorted by the first index of each tuple
    if (len(arr) > 1):
        half = int(len(arr)/2) 
        arr1 = mergeSort(splitArrBot(arr, half), elmt)
        arr2 = mergeSort(splitArrTop(arr, half), elmt)
        return mergeArr(arr1, arr2, elmt)
    else :
        return arr


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
