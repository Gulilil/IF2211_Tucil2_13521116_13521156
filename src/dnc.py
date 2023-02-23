from calculate import *

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
        newAmount2 = amount // 2
        if (not ((amount // 2) % 2 == 0)):
            newAmount2 = (amount // 2) + 1

        newAmount = amount - (amount // 2)
        
        # print("newAmount" + str(newAmount))
        # print("newAmount2" + str(newAmount2))

        for i in range (newAmount2):
            arr1.append(arr[i])  
        arr2 = []
        for i in range (amount // 2, amount):
            arr2.append(arr[i])

        d1 = getClosestPairDnc(arr1, newAmount2)
        d2 = getClosestPairDnc(arr2, newAmount2)
        if (d1 < d2):
            d = d1
        else:
            d = d2
        
        # listing all points in range of d from line l (mid line of all points)
        points = []
        for i in range (newAmount2):
            if (arr[i][0] >= arr2[i][0] - int(d) or arr[i][0] <= arr2[i][0] + int(d)):
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

