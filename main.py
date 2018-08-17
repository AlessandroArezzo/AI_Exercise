from Robot import Robot,RobotState
from matplotlib import pyplot as plt
from search import breadth_first_tree_search,depth_first_tree_search,iterative_deepening_search
from scipy.spatial import Voronoi, voronoi_plot_2d
import utils
import matplotlib.animation as animation
import matplotlib
import random
import numpy as np


points=[(0,0),(1,1),(2,1),(3,3),(5,4),(5,8),(10,8)]

matrix=[[(0,0),(1,1),(2,1)],[(1,1),(0,0),(2,1),(3,3)],[(2,1),(0,0),(1,1),(5,4)],[(3,3),(5,4),(5,8)],[(5,8),(3,3),(10,8)],[(10,8),(5,4),(5,8)]]

"""matrix=utils.createPlot(points)"""


for region in matrix:
    for i in range(1,region.__len__()):
        plt.plot([region[0][0],region[i][0]],[region[0][1],region[i][1]],'black')

plt.xlim(0,11)
plt.ylim(0,9)


robot=Robot(points[0],points[6],matrix)
breadth_first_tree_search(robot)

"""plt.show()"""

# Alternativa ? usare Delauney (sempre in scipy.spatial) al posto di Voronoi. Delauney infatti ha anche un metodo neighbors he potrebbe permettere di ottenere i vertici collegati ad un certo vertice
