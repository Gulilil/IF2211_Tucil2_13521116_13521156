from calculate import *

def notQualified(point1, point2, d):
    for i in range (len(point1)):
        if (abs(point1[i] - point2[i]) > d):
            return True
    return False

def getClosestPairDnc(arr, amount):
    # points in arr are already arranged by the absis 
    arrSolution = []
    if (amount == 2):
        arrSolution.append(0, 1)
        d = getDistance(arr[0], arr[1])
    else: 
        arr1 = []
        for i in range (amount/2):
            arr1.append(arr[i]) 
        arr2 = []
        for i in range (amount/2, amount + 1):
            arr2.append(arr[i])
        d1 = getClosestPairDnc(arr1, amount/2)
        d2 = getClosestPairDnc(arr2, amount/2)
        if (d1 < d2):
            d = d1
        else:
            d = d2
        
    # listing all points in range of d from line l (mid line of all points)
    points = []
    for i in range (amount):
        if (arr[i][0] >= arr2[0] - d or arr[i][0] <= arr2[0] + d):
            points.append(arr[i])

    # sort by the ordinat 

    for i in range (len(points)):
        for j in range (i+1, len(points)):
           if (notQualified(points[i], points[j], d)):
               continue
           else:
               d3 = getDistance(points[i], points[j])
               if (d3 < d):
                   d = d3

    return d

