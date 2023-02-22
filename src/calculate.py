import random
import time

# Contains calculation of Divide and Conquer Algorithm

# Random Number
def generateNumber(length, boundaries):
    # Generate random number (float) and inserting it into a tuple
    # Generated random number will be in range of (-boundaries < x < boundaries)
    container = [];
    for i in range (length):
        container.append(random.uniform(-boundaries, boundaries))
    return tuple(container)

# Time
def startTime():
    return time.time()  

def stopTime():
    return time.time()

def convertToSeconds(micros):
    return micros* (10 ** 6);




