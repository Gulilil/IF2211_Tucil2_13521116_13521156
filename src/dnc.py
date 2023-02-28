from calculate import *


# ===================================================
# Calculation for Divide and Conquer Algorithm
def notQualified(point1, point2, d):
    for i in range (len(point1)):
        if (abs(point1[i] - point2[i]) > d):
            return True
    return False

def getClosestPairof3(p1, p2, p3):
    d1 = getDistance(p1, p2)
    d2 = getDistance(p2, p3)
    d3 = getDistance(p3, p1)
    
    if (min(d1,d2,d3) == d1):
        return [(p1,p2)]
    elif (min(d1,d2,d3) == d2):
        return [(p2,p3)]
    else :
        return [(p1,p3)]

def getSolutionDnC(arr, amount):
    arr = mergeSort(arr,0)
    if (amount == 2):
        return [(arr[0], arr[1])]
    elif (amount == 3):
        return getClosestPairof3(arr[0], arr[1], arr[2]);
    else :
        # split array into 2
        newAmount = amount // 2
        arr1 = splitArrBot(arr, newAmount)
        arr2 = splitArrTop(arr, newAmount)

        # get closest points of left side  and right side
        ptuple1 = getSolutionDnC(arr1, newAmount)
        ptuple2 = getSolutionDnC(arr2, newAmount)

        if (getDistance(ptuple1[0][0], ptuple1[0][1]) < getDistance(ptuple2[0][0], ptuple2[0][1])):
            ptuple2.clear()
        elif (getDistance(ptuple1[0][0], ptuple1[0][1]) == getDistance(ptuple2[0][0], ptuple2[0][1])):
            ptuple1.append(ptuple2[0])
            ptuple2.clear()
        else :
            ptuple1.clear()
            for i in range(len(ptuple2)):
                ptuple1.append(ptuple2[i])
            ptuple2.clear()
        
        #shortest points will be stored in ptuple1
        return thirdCase(arr, ptuple1, amount)


def thirdCase(arr, tupleP, amount):
    # calculate minimal distance
    d = getDistance(tupleP[0][0], tupleP[0][1])
    # default answer will be the points from tupleP
    # will be changed if there is any other shorter pair
    result = []
    if (amount == 2):
        return tupleP
    else :
        points = []
        newAmount = amount // 2

        # Insert points within d range
        for i in range(amount):
            if (arr[i][0] >= arr[newAmount][0] - int(d) + 1 
                or arr[newAmount][0] + int(d) + 1):
                points.append(arr[i])
        
        # Sort based on the second element (y-axis)
        points = mergeSort(points, 1)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                # case the point is outside the d range

                if (notQualified(points[i], points[j], d)):
                    continue
                else :
                    if (getDistance(points[i], points[j]) < d):
                        result.clear()
                        result.append((points[i], points[j]))
                        d = getDistance(points[i], points[j])
                    elif (getDistance (points[i], points[j]) == d):
                        result.append((points[i], points[j]))
    return result


# Ini hanya untuk ngetest aja
# array = [(1,2,3),
#          (-18,4,5),
#          (2,1,3),
#          (-18,5,4),
#          (6,7,8),
#          (8,5,6),
#          (-20, 4, 7),
#          (-6, -8, 5),
#          (-10, 5, -9),
#          (-3, -2, -8)
#         ]

