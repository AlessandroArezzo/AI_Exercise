from Robot import Robot
from search import breadth_first_tree_search,depth_first_tree_search,depth_limited_search,iterative_deepening_search,best_first_graph_search,astar_search,greedy_best_first_graph_search,runSearchers
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
        problem = Robot(initialPoint, goalPoint, matrix)

        searchers=[breadth_first_tree_search,depth_first_tree_search,depth_limited_search,iterative_deepening_search,greedy_best_first_graph_search,astar_search]
        runSearchers(problem,points,searchers,limit)
    else:
        break