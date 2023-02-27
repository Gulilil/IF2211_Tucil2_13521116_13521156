import matplotlib.pyplot as plt

def visualize(arr, points1, points2, amount, dimension, boundary):
    fig = plt.figure()
    if (dimension == 3):
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
            if ((x == points1[0] and y == points1[1] and z == points1[2]) or
                (x == points2[0] and y == points2[1] and z == points2[2])):
                ax.scatter(x, y, z, c='red')
            else:
                ax.scatter(x, y, z, c='black')
    else :
        ax = plt.axes(projection='2d')
        ax.set_title('Closest Pair of Dots in 2D')
        dots = []
        for i in range (boundary + 1):
            dots.append(i)

        ax.scatter(dots, dots, c='white', alpha=0)
        for i in range (amount):
            x = arr[i][0]
            y = arr[i][1]
            if ((x == points1[0] and y == points1[1]) or
                (x == points2[0] and y == points2[1])):
                ax.scatter(x, y, c='red')
            else:
                ax.scatter(x, y, c='black')

    plt.show()