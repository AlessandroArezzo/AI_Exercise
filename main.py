from Robot import Robot
from search import breadth_first_tree_search,depth_first_tree_search,depth_limited_search,iterative_deepening_search,best_first_graph_search,astar_search
import utils

#points=[(0,0),(1,1),(2,1),(3,3),(5,4),(5,8),(8,4),(6,3),(10,8)]

#matrix=[[(0,0),(1,1),(2,1)],[(1,1),(0,0),(2,1),(3,3)],[(2,1),(0,0),(1,1),(5,4),(6,3)],[(3,3),(5,4),(5,8)],[(5,4),(10,8)],[(5,8),(3,3),(10,8)],[(8,4),(5,4),(10,8)],[(6,3),(2,1),(10,8)],[(10,8),(5,4),(5,8),(8,4),(6,3)]]

#Istanzia il problema
points=utils.generateRandomPoints(10,0,20)
matrix=utils.createGridActions(points)
initialPoint=utils.searchInitialPoint(points)
goalPoint=utils.searchGoalPoint(points)
robot=Robot(initialPoint,goalPoint,matrix)

#breadth_first_tree_search
print "breadth_first_tree_search"
node_result=breadth_first_tree_search(robot)
path_result=node_result.path()
print "RESULT breadth_first_tree_search"
utils.printResult(matrix,path_result,"Breadth_first_tree_search",points,initialPoint,goalPoint)

#depth_first_tree_search
print "depth_first_tree_search"
node_result=depth_first_tree_search(robot)
path_result=node_result.path()
print "RESULT depth_first_tree_search"
utils.printResult(matrix,path_result,"Depth_first_tree_search",points,initialPoint,goalPoint)

#depth_first_tree_search
print "depth_first_tree_search"
node_result=depth_limited_search(robot)
path_result=node_result.path()
print "RESULT depth_limited_search"
utils.printResult(matrix,path_result,"Depth_limited_search",points,initialPoint,goalPoint)

#iterative_deepening_search
print "iterative_deepening_search"
node_result=iterative_deepening_search(robot)
path_result=node_result.path()
print "RESULT iterative_deepening_search"
utils.printResult(matrix,path_result,"Iterative_deepening_search",points,initialPoint,goalPoint)


#best_first_graph_search
print "best_first_graph_search"
node_result=best_first_graph_search(robot,robot.h)
path_result=node_result.path()
print "RESULT best_first_graph_search"
utils.printResult(matrix,path_result,"Best_first_graph_search",points,initialPoint,goalPoint)

#astar_search
print "astar_search"
node_result=astar_search(robot,robot.h)
path_result=node_result.path()
print "RESULT astar_search"
utils.printResult(matrix,path_result,"Astar_search",points,initialPoint,goalPoint)

