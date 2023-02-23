
# Contain input and output algorithm

# Display Ascii Art
# nanti aja ini kalo sempet

# Title Printing
def displayTitle(title):
    # Displaying title
    length = len(title)
    if ((36 - length) %2 == 0):
        fspace = int((36 - length)/2)
        bspace = fspace
    else:
        fspace = int((36 - length +1)/2)
        bspace = fspace -1
    print("============================================")
    print("====", end="") ; print(" "*fspace, end="")
    print(title, end="") 
    print(" "*bspace, end=""); print("====")
    print("============================================")


# User Input
def askUserInput():
    # Return tuple of three value, amount of points, dimension, and boundaries
    amount = input("Amount of points you want to insert: ")
    dimension = input("Dimension of Euclidean Space you want to use: ")
    boundaries = input("Boundaries of Euclidean Space you want to use: ")
    try:
        amount = int(amount)
        dimension = int(dimension)
        boundaries = float(boundaries)
        return (amount, dimension, boundaries)
    except:
        return (None, None, None)

def validateUserInput():
    data = askUserInput()
    valid = False
    while (not valid):
        valid = True
        if (data[0] == None):
            print(" => (Some of) the answers you just inserted cannot be converted into integer or float.")
            valid = False
        elif (data[0] < 2 or data[1] < 3):
            print(" => The minimum amount of points are 2 and the minimum dimensions of Euclidean Plane are 3")
            valid = False

        if (not valid):
            print(" => Please insert again.")
            data = askUserInput()
    return data
    
# Displaying Arr
def displayArr(arr):
    for i in range(len(arr)):
        print(arr[i]);


