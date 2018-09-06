from search import breadth_first_tree_search,depth_limited_search,iterative_deepening_search,breadth_first_graph_search,astar_search,depth_first_graph_search,greedy_best_first_graph_search,runSearchers
from scipy.spatial import Delaunay
import utils
from Robot import Robot
import os
import time
import psutil

menu=0
f=None
while(True):
    nPoints = 0
    min = 1
    max = 0
    limit = -1
    print "--Inserisci 1 per eseguire tutti gli algoritmi mostrando i risultati graficamente"
    print "--Inserisci 2 per eseguire delle prove su un certo algortimo"
    print "--Inserisci qualsiasi altro valore per uscire"
    menu=input()
    #Se utente ha inserito un valore diverso da 1 e da 2, si chiude il programma
    if(menu!=1 and menu!=2):
        break

    #Altrimenti si richiede inserimento del numero di punti che rappresenteranno gli stati del problema ed il range delle relative coordinate
    try:
        while (nPoints < 3):
            nPoints = input("Inserisci numero di punti in cui suddividere il piano (Inserire valore maggiore uguale a 3)\n")
        while (min >= max):
            min = input("Inserisci limite inferiore dei valori dei punti\n")
            max = input("Inserisci limite superiore dei valori dei punti\n")
    except:
        print("Inserisci dei valori numerici corretti")
    # Se l'utente ha inserito uno nel men?, si richiede di inserire la profondit? limite per la ricerca ad approfondimento limitato
    if menu==1:
        try:
            while (limit < 0):
                limit = input("Inserisci la profondita' con la quale eseguire l'algoritmo Depth_limited_search (Inserire valore positivo)\n")
        except:
            print("Inserisci dei valori numerici corretti")
        #Genera punti casualmente
        points = utils.generateRandomPoints(nPoints, min, max)
        #Effettuaffettua suddivisione del piano in poligoni aventi per vertici i punti generati
        triang = Delaunay(points)
        #Costruisce il dizionario che associa ad ogni punto i suoi vicini nel piano diviso in poligoni
        dictActions = utils.createDict(points, triang)
        #Si definiscono i punti iniziale (quello pi? a sx nel piano) e obiettivo (quello pi? a dx)
        initialPoint = utils.searchInitialPoint(points)
        goalPoint = utils.searchGoalPoint(points)
        """Instanzia il problema e lancia metodo runSearchers a cui si passano i nomi delle funzioni che implementano gli algortimi 
        da eseguire ed il limite della profondit? di taglio"""
        problem = Robot(initialPoint, goalPoint, dictActions)
        searchers=[breadth_first_tree_search,breadth_first_graph_search,depth_first_graph_search,depth_limited_search,iterative_deepening_search,greedy_best_first_graph_search,astar_search]
        runSearchers(problem,points,searchers,limit)
    elif menu==2:
        #Richiede quale algoritmo si vuole testare
        print "--Inserisci 1 per testare algoritmo breadth first tree search"
        print "--Inserisci 2 per testare algoritmo breadth first graph search"
        print "--Inserisci 3 per testare algoritmo depth first graph search"
        print "--Inserisci 4 per testare algoritmo iterative deepening search"
        print "--Inserisci 5 per testare algoritmo greedy best first graph search"
        print "--Inserisci 6 per testare algoritmo astar_search"
        alg=input()
        """Sulla base del codice inserito dall'utente imposta la variabile f con il nome dell'algoritmo da eseguire"""
        if alg==1:
            f=breadth_first_tree_search
        elif alg==2:
            f=breadth_first_graph_search
        elif alg==3:
            f=depth_first_graph_search
        elif alg==4:
            f=iterative_deepening_search
        elif alg==5:
            f=greedy_best_first_graph_search
        elif alg==6:
            f=astar_search
        else:
            break
        #Richiede numero di esperimenti da eseguire
        n_exec=input("Inserisci numero di esperimenti da effettuare\n")
        sumTime = 0
        sumCost = 0
        sumDepth = 0
        sumMemory = 0
        #Esegue algoritmo per il numero di volte eseguito, ad ogni iterazione lo esegue su una istanza diversa
        for i in range(0, n_exec):
            print "EXPERIMENT: "+unicode(i)
            points = utils.generateRandomPoints(nPoints, min, max)
            triang = Delaunay(points)
            dictActions = utils.createDict(points, triang)
            initialPoint = utils.searchInitialPoint(points)
            goalPoint = utils.searchGoalPoint(points)
            problem = Robot(initialPoint, goalPoint, dictActions)
            start = time.time()
            node_result = f(problem)
            sumTime += time.time() - start
            sumCost += node_result.path_cost
            sumDepth += node_result.depth
            pid = os.getpid()
            py = psutil.Process(pid)
            sumMemory += (py.memory_info()[0] / 1024 / 1024)

        print "RESULTS:\nTime: " + unicode(sumTime / n_exec) + "--Cost: " + unicode(
            sumCost / n_exec) + "--Depth: " + unicode(sumDepth / n_exec) +"--Memory: " + unicode(sumMemory / n_exec)

