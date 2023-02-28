import matplotlib.pyplot as plt

def visualize(arr, solutions, amount, dimension, boundary):
    if (dimension == 3):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.set_title('Closest Pair of Dots in 3D')
        dots = []
        for i in range (boundary + 1):
            dots.append(i)
        print(dots)
        ax.scatter(dots, dots, dots, c='white', alpha=0)
        for i in range (amount):
            x = arr[i][0]
            y = arr[i][1]
            z = arr[i][2]
            ax.scatter(x, y, z, c='black')
        for i in range(len(solutions)):
            for j in range(2):
                x = solutions[i][j][0]
                y = solutions[i][j][1]
                z = solutions[i][j][2]
                ax.scatter(x,y,z, c="red")
        plt.show()
    else :
        fig = plt.figure()
        ax = plt.axes()
        ax.set_title('Closest Pair of Dots in 2D')
        dots = []
        for i in range (boundary + 1):
            dots.append(i)
        print(dots)
        ax.scatter(dots, dots, c='white', alpha=0)
        for i in range (amount):
            x = arr[i][0]
            y = arr[i][1]
            ax.scatter(x, y, c='black')
        for i in range(len(solutions)):
            for j in range(2):
                x = solutions[i][j][0]
                y = solutions[i][j][1]
                ax.scatter(x,y, c="red")
        plt.show()