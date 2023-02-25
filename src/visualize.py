import numpy as np 
import matplotlib.pyplot as plt

def visualize(arr, points1, points2, amount, boundary):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set_title('Closest Pair of Dots in 3D')
    dots = []
    for i in range (boundary + 1):
        dots.append(i)
    ax.scatter(dots, dots, dots, c='white', alpha=0)
    for i in range (amount):
        x = arr[i][0]
        y = arr[i][1]
        z = arr[i][2]
        ax.scatter(x, y, z, c='black')

    plt.show()