from Robot import Robot
from search import breadth_first_tree_search,depth_first_tree_search,depth_limited_search,iterative_deepening_search,best_first_graph_search,astar_search
import utils
from scipy.spatial import Delaunay

while(True):
    nPoints=0
    min=1
    max=0
    limit=-1
    input_command=input("--Inserisci 1 per immettere i dati del problema \n--Inserisci qualsiasi altro carattere per uscire\n")
    if(input_command==1):
        while(True):
            try:
                while(nPoints<3):
                    nPoints=input("Inserisci numero di punti in cui suddividere il piano (Inserire valore maggiore uguale a 3)\n")
                while(min>=max):
                    min=input("Inserisci limite inferiore dei valori dei punti\n")
                    max=input("Inserisci limite superiore dei valori dei punti\n")
                while(limit<0):
                    limit=input("Inserisci la profondita' con la quale eseguire l'algoritmo Depth_limited_search (Inserire valore positivo)\n")
                break
            except:
                print("Inserisci dei valori numerici corretti")

        # Istanzia il problema
        points = utils.generateRandomPoints(nPoints, min, max)
        triang = Delaunay(points)
        vertices = triang.vertices
        matrix = utils.createGrid(points, vertices)
        initialPoint = utils.searchInitialPoint(points)
        goalPoint = utils.searchGoalPoint(points)
        robot = Robot(initialPoint, goalPoint, matrix)

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

        # depth_first_tree_search
        print "depth_first_tree_search"
        node_result = depth_limited_search(robot, limit)
        if node_result == 'cutoff':
            print "Problema non risolvibile ponendo come limite di profondita' " + unicode(limit)
        elif node_result == None:
            print "Il problema non ha soluzione"
        else:
            path_result = node_result.path()
            print "RESULT depth_limited_search"
            utils.printResult(matrix, path_result, "Depth_limited_search", points, initialPoint, goalPoint)

        # iterative_deepening_search
        print "iterative_deepening_search"
        node_result = iterative_deepening_search(robot)
        path_result = node_result.path()
        print "RESULT iterative_deepening_search"
        utils.printResult(matrix, path_result, "Iterative_deepening_search", points, initialPoint, goalPoint)

        # best_first_graph_search
        print "best_first_graph_search"
        node_result = best_first_graph_search(robot, robot.h)
        path_result = node_result.path()
        print "RESULT best_first_graph_search"
        utils.printResult(matrix, path_result, "Best_first_graph_search", points, initialPoint, goalPoint)

        # astar_search
        print "astar_search"
        node_result = astar_search(robot, robot.h)
        path_result = node_result.path()
        print "RESULT astar_search"
        utils.printResult(matrix, path_result, "Astar_search", points, initialPoint, goalPoint)

    else:
        break

