from calculate import *


# ===================================================
# Calculation for Divide and Conquer Algorithm
def notQualified(point1, point2, d):
    for i in range (len(point1)):
        if (abs(point1[i] - point2[i]) > d):
            return True
    return False

def getClosestPairDnc(arr, amount):
    arr = mergeSort(arr, 0)
    # arrSolution = []
    if (amount == 2):
        d = getDistance(arr[0], arr[1])
    else: 
        arr1 = []
        newAmount = amount // 2
        # print("newAmount(1)" + str(newAmount2))
        if (amount // 2 == 1):
            newAmount = (amount // 2) + 1
        
        # print("newAmount" + str(newAmount))
        # print("newAmount2" + str(newAmount2))

        for i in range (newAmount):
            arr1.append(arr[i])  
        arr2 = []
        for i in range (amount // 2, amount):
            arr2.append(arr[i])

        d1 = getClosestPairDnc(arr1, newAmount)
        d2 = getClosestPairDnc(arr2, newAmount)
        if (d1 < d2):
            d = d1
        else:
            d = d2
        

    return d

def getSolutionDnC(arr, d, amount):
        # listing all points in range of d from line l (mid line of all points)
    if (amount == 2):
        return d        
    else:
        points = []
        newAmount2 = amount // 2
        for i in range (amount):
            if (arr[i][0] >= arr[newAmount2][0] - int(d) + 1 or arr[i][0] <= arr[newAmount2][0] + int(d) + 1):
                points.append(arr[i])

        points = mergeSort(points, 1)

        for i in range (len(points)):
            for j in range (i+1, len(points)):
                if (notQualified(points[i], points[j], d)):
                    continue
                else:
                    d3 = getDistance(points[i], points[j])
                    if (d3 < d):
                        d = d3
    return d