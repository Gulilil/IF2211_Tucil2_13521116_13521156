EuclideanCountDnC = 0
EuclideanCountBF = 0


def addCountsDnC(n):
    global EuclideanCountDnC 
    EuclideanCountDnC += n

def addCountsBF(n):
    global EuclideanCountBF
    EuclideanCountBF += n

def getCountsDnC():
    global EuclideanCountDnC
    return EuclideanCountDnC

def getCountsBF():
    global EuclideanCountBF
    return EuclideanCountBF