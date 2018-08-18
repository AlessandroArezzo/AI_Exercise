
import os
from utils import FIFOQueue,PriorityQueue,Stack,memoize
import psutil
import sys



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

class Node:

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state=state
        self.parent=parent
        self.action=action
        self.path_cost=path_cost
        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth=0

    def __repr__(self):
        """(pf) Modified to display depth, f and h"""
        if hasattr(self,'f'):
            return "<Node: f=%d, depth=%d, h=%d\n%s>" % (self.f,
                                                         self.depth,
                                                         self.h,
                                                         self.state)
        else:
            return "<Node: depth=%d\n%s, Cost:%f>" % (self.depth,self.state,self.path_cost)

    def path(self):
        """Ricostruisce il cammino dal nodo corrente alla radice"""
        x, result = self, [self]
        while x.parent:
            result.append(x.parent)
            x = x.parent
        return result

    def expand(self, problem):
        """Per ogni coppia (action, state) restituita dal metodo successor a partire dallo stato corrispondente
         al nodo in cui ci si trova (self, siamo nella classe Node) ed il quale si passa a successor stesso,
         si crea un oggetto Node. Si ritornano infine tutti i nodi creati (la frontiera espansa)
        
        return [Node(next_state, self, action,
                     problem.path_cost(self.path_cost, self.state, action, next_state))
                for (action, next_state) in problem.successor(self.state)]"""
        return[Node(next_state, self, action,
                   problem.path_cost(self.path_cost, self.state, action, next_state))
        for (action, next_state) in problem.successor(self.state)]




# Uninformed Search algorithms

def tree_search(problem,fringe):
    fringe.append(Node(problem.initial))
    max_depth = 0
    while fringe:
        node=fringe.pop()
        if node.depth > max_depth:
            max_depth = node.depth
            if max_depth < 50 or max_depth % 1000 == 0:
                pid = os.getpid()
                py = psutil.Process(pid)
                memoryUse = py.memory_info()[0] / 1024 / 1024
                print('Reached depth', max_depth,
                      'Open len', len(fringe),
                      'Memory used (MBytes)', memoryUse)
        print node #stampa nodo espanso
        if problem.goal_test(node.state):
            return node
        newNode=node.expand(problem)
        fringe.extend(newNode)
    return None



def breadth_first_tree_search(problem):
    return tree_search(problem, FIFOQueue())


def depth_first_tree_search(problem):
    return tree_search(problem, Stack())


def depth_limited_search(problem, limit=10):
    "[Fig. 3.12]"
    def recursive_dls(node, problem, limit):
        cutoff_occurred = False
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
    # Body of depth_limited_search:
    return recursive_dls(Node(problem.initial), problem, limit)

def iterative_deepening_search(problem):
    "[Fig. 3.13]"
    for depth in xrange(sys.maxint):
        result = depth_limited_search(problem, depth)
        pid = os.getpid()
        py = psutil.Process(pid)
        memoryUse = py.memory_info()[0]/1024/1024
        print('end depth_limited_search at depth', depth, 'mem (GBytes)', memoryUse)
        if result is not 'cutoff':
            return result

def graph_search(problem, fringe):
    """Search through the successors of a problem to find a goal.
    The argument fringe should be an empty queue.
    If two paths reach a state, only use the best one. [Fig. 3.18]"""
    closed = {}
    fringe.append(Node(problem.initial))
    max_depth = 0
    while fringe:
        node = fringe.pop()
        # Print some information about search progress
        if node.depth > max_depth:
            max_depth = node.depth
            if max_depth < 50 or max_depth % 1000 == 0:
                pid = os.getpid()
                py = psutil.Process(pid)
                memoryUse = py.memory_info()[0] / 1024 / 1024
                print('Reached depth', max_depth,
                      'Open len', len(fringe),
                      'Memory used (MBytes)', memoryUse)

        if problem.goal_test(node.state):
            return node
        serial = node.state.__str__()
        if serial not in closed:
            closed[serial] = True
            fringe.extend(node.expand(problem))
    return None

def breadth_first_graph_search(problem):
    "Search the shallowest nodes in the search tree first. [p 74]"
    return graph_search(problem, FIFOQueue())

def depth_first_graph_search(problem):
    "Search the deepest nodes in the search tree first. [p 74]"
    return graph_search(problem, Stack())

# Informed (Heuristic) Search
def best_first_graph_search(problem, f):
    f = memoize(f, 'f')
    return graph_search(problem, PriorityQueue(min, f))