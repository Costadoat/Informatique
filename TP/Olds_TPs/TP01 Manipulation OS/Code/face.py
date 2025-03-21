from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from array import array

import matplotlib.pyplot as plt

import numpy as np

import csv



X1 = []

Y1 = []

Z1 = []



cr = csv.reader(open("data.csv"))



for row in cr:

    X1.append(float(row[0]))

    Y1.append(float(row[1]))

    Z1.append(float(row[2]))



X = np.asarray(X1)

Y = np.asarray(Y1)

Z = np.asarray(Z1)


fig = plt.figure()

ax = fig.gca(projection='3d')

surf = ax.scatter(X, Y, Z)



plt.show()



