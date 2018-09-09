from utils import FIFOQueue,PriorityQueue,Stack
import psutil
import sys
import utils
import os
import time

#Variabile globale sum_memory e' utilizzata per tener traccia della quantita' di memoria totale utilizzata nell'eseguire una serie di esperimenti
sum_memory=0

def init_sumMemory():
    sum_memory=0

def get_sumMemory():
    return sum_memory

"""Definizione della classe problem che fornisce un implementazione di default per l'interfaccia di un generico problema"""
class Problem:

    def __init__(self,initial,goal):
        self.initial = initial
        self.goal = goal

    def successor(self, state):
        pass  # abstract

    def goal_test(self, state):
        return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

"""Definizione della classe Node che rappresenta i nodi dell'albero/grafo di ricerca"""
class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state=state
        self.parent=parent
        self.action=action
        self.path_cost=path_cost
        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth=0

    def __repr__(self):
        return "<Node: depth=%d\n%s, Cost:%f>" % (self.depth,self.state,self.path_cost)

    def path(self):
        """Ricostruisce il cammino dal nodo corrente alla radice"""
        x, result = self, [self]
        while x.parent:
            result.append(x.parent)
            x = x.parent
        return result

    def expand(self, problem):
        """
        Per ogni coppia (action, state) restituita dal metodo successor a partire dallo stato corrispondente
         al nodo in cui ci si trova, si crea un oggetto Node. Si ritornano infine tutti i nodi creati (la frontiera espansa)
        """
        return[Node(next_state, self, action,
                   problem.path_cost(self.path_cost, self.state, action, next_state))
        for (action, next_state) in problem.successor(self.state)]


# Uninformed Search algorithms

"""Ricerca su albero, stampa informazioni sull'avanzamento dell'esecuzione"""
def tree_search(problem,fringe):
    fringe.append(Node(problem.initial))
    max_depth = 0
    global sum_memory
    while fringe:
        node=fringe.pop()
        if node.depth > max_depth:
            max_depth = node.depth
            if max_depth < 50 or max_depth % 1000 == 0:
                pid = os.getpid()
                py = psutil.Process(pid)
                memoryUse = py.memory_info()[0] / 1024 / 1024
                print ("Reached depth: "+ unicode(max_depth)+" Open len: "+ unicode(len(fringe))+" Memory used (MBytes): "+ unicode(memoryUse))
        if problem.goal_test(node.state):
            sum_memory+=memoryUse
            return node
        newNode=node.expand(problem)
        fringe.extend(newNode)
    return None



def breadth_first_tree_search(problem):
    return tree_search(problem, FIFOQueue())


def depth_first_tree_search(problem):
    return tree_search(problem, Stack())

"""Ricerca a profondita' limitata. Utilizza un implementazione che prevede di tenere traccia in un dizionario degli stati gia' visitati"""
def depth_limited_search(problem, limit=10):
    closed={}
    def recursive_dls(node, problem, limit):
        cutoff_occurred = False
        serial = node.state.__str__()
        if serial not in closed:
            closed[serial] = True
            if problem.goal_test(node.state):
                return node
            elif node.depth == limit:
                return 'cutoff'
            else:
                for successor in node.expand(problem):
                    result = recursive_dls(successor, problem, limit)
                    if result == 'cutoff':
                        cutoff_occurred = True
                    elif result != None:
                        return result
            if cutoff_occurred:
                return 'cutoff'
            else:
                return None
        else:
            return None
    return recursive_dls(Node(problem.initial), problem, limit)

def iterative_deepening_search(problem):
    global sum_memory
    for depth in xrange(sys.maxint):
        result = depth_limited_search(problem, depth)
        pid = os.getpid()
        py = psutil.Process(pid)
        memoryUse = py.memory_info()[0]/1024/1024
        print("end depth_limited_search at depth "+unicode(depth)+ " mem (GBytes) "+unicode(memoryUse))
        if result is not 'cutoff':
            sum_memory+=memoryUse
            return result

"""Ricerca su grafo, stampa informazioni sull'avanzamento dell'esecuzione"""
def graph_search(problem, fringe):
    closed = {}
    fringe.append(Node(problem.initial))
    max_depth = 0
    global sum_memory
    while fringe:
        node = fringe.pop()
        if node.depth > max_depth:
            max_depth = node.depth
            if max_depth < 50 or max_depth % 1000 == 0:
                pid = os.getpid()
                py = psutil.Process(pid)
                memoryUse = py.memory_info()[0] / 1024 / 1024
                print ("Reached depth: "+ unicode(max_depth)+" Open len: "+ unicode(len(fringe))+" Memory used (MBytes): "+ unicode(memoryUse))
        if problem.goal_test(node.state):
            sum_memory+=memoryUse
            return node
        serial = node.state.__str__()
        if serial not in closed:
            closed[serial] = True
            fringe.extend(node.expand(problem))
    return None

def breadth_first_graph_search(problem):
    return graph_search(problem, FIFOQueue())

def depth_first_graph_search(problem):
    return graph_search(problem, Stack())

# Informed (Heuristic) Search
"""Ricerche euristiche utilizzano algoritmo di ricerca su grafo"""

def best_first_graph_search(problem, f):
    return graph_search(problem, PriorityQueue(min, f))

def greedy_best_first_graph_search(problem,h=None):
    h = h or problem.h
    def f(n):
        return h(n)
    return best_first_graph_search(problem, f)

def astar_search(problem, h=None):
    h = h or problem.h
    def f(n):
        priority= n.path_cost + h(n)
        return priority
    return best_first_graph_search(problem, f)

"""runSearchers esegue gli algoritmi ricevuti come parametri e stampa i risultati invocando la funzione printResult 
definita in utils.py."""
def runSearchers(problem,points,searchers=[breadth_first_tree_search,depth_first_tree_search,depth_limited_search,iterative_deepening_search,greedy_best_first_graph_search,astar_search],limit=10):
    for s in searchers:
        print ("Running %s" % s.__name__)
        if (s == depth_limited_search):
            start=time.time()
            node_result = s(problem, limit)
            elapsed=time.time()-start
        else:
            start=time.time()
            node_result = s(problem)
            elapsed=time.time()-start
        print("Elapsed time: " +unicode(elapsed )+ "seconds")
        if(node_result==None):
            print("Non trovata soluzione con l'algoritmo "+s.__name__)
        elif(node_result=='cutoff'):
            print("Non trovata soluzione con l'algoritmo "+s.__name__+" e limite di profondita' "+unicode(limit))
        else:
            path_result = node_result.path()
            print ("Printing result...")
            utils.printResult(problem.dictActions, path_result, s.__name__, points, problem)
