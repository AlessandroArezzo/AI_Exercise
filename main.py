from Robot import Robot,RobotState
from matplotlib import pyplot as plt
from search import breadth_first_tree_search,depth_first_tree_search,depth_limited_search,iterative_deepening_search,best_first_graph_search,astar_search
from scipy.spatial import Voronoi, voronoi_plot_2d
import utils
import matplotlib.animation as animation
import matplotlib
import random
import numpy as np
import time


points=[(0,0),(1,1),(2,1),(3,3),(5,4),(5,8),(8,4),(10,8)]

matrix=[[(0,0),(1,1),(2,1)],[(1,1),(0,0),(2,1),(3,3)],[(2,1),(0,0),(1,1),(5,4)],[(3,3),(5,4),(5,8),(10,8)],[(5,4),(10,8)],[(5,8),(3,3),(10,8)],[(8,4),(5,4),(10,8)],[(10,8),(5,4),(5,8),(3,3),(8,4)]]

"""matrix=utils.createPlot(points)"""

fig=plt.figure()

for region in matrix:
    for i in range(1,region.__len__()):
        plt.plot([region[0][0],region[i][0]],[region[0][1],region[i][1]],'black',)

plt.xlim(0,11)
plt.ylim(0,9)


print "breadth_first_tree_search"
robot=Robot(points[0],points[points.__len__()-1],matrix)
node_result=breadth_first_tree_search(robot)

path_result=node_result.path()
print "RESULT breadth_first_tree_search"
for node in reversed(path_result):
    print node

plt.title("breadth_first_tree_search")
plt.draw()
plt.show(block=False)
plt.pause(0.001)
for node in reversed(path_result):
    if(node.parent):
        plt.pause(0.1)
        plt.plot([node.parent.state.x,node.state.x],[node.parent.state.y,node.state.y],'-r')
        time.sleep(1.5)


time.sleep(10)

print "depth_first_tree_search"

node_result=depth_first_tree_search(robot)

path_result=node_result.path()
print "RESULT depth_first_tree_search"
for node in path_result:
    print node

print "depth_limited_search"

node_result=depth_limited_search(robot)

path_result=node_result.path()
print "RESULT depth_limited_search"
for node in path_result:
    print node

print "iterative_deepening_search"

node_result=iterative_deepening_search(robot)

path_result=node_result.path()
print "RESULT iterative_deepening_search"
for node in path_result:
    print node


print "best_first_graph_search"

node_result=best_first_graph_search(robot,robot.h)

path_result=node_result.path()
print "RESULT best_first_graph_search"
for node in path_result:
    print node

print "astar_search"

node_result=astar_search(robot,robot.h)

path_result=node_result.path()
print "RESULT astar_search"
for node in path_result:
    print node



# Alternativa ? usare Delauney (sempre in scipy.spatial) al posto di Voronoi. Delauney infatti ha anche un metodo neighbors he potrebbe permettere di ottenere i vertici collegati ad un certo vertice
