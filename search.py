
import os
from utils import FIFOQueue,PriorityQueue,Stack,infinity,memoize,name,print_table,update

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
        self.update(self, state=state, parent=parent, action=action,
               path_cost=path_cost, depth=0)
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        """(pf) Modified to display depth, f and h"""
        if hasattr(self,'f'):
            return "<Node: f=%d, depth=%d, h=%d\n%s>" % (self.f,
                                                         self.depth,
                                                         self.h,
                                                         self.state)
        else:
            return "<Node: depth=%d\n%s>" % (self.depth,self.state)

    def path(self):
        "Create a list of nodes from the root to this node."
        x, result = self, [self]
        while x.parent:
            result.append(x.parent)
            x = x.parent
        return result

    def expand(self, problem):
        """Per ogni coppia (action, state) restituita dal metodo successor a partire dallo stato corrispondente
         al nodo in cui ci si trova (self, siamo nella classe Node) ed il quale si passa a successor stesso,
         si crea un oggetto Node. Si ritornano infine tutti i nodi creati (la frontiera espansa)"""
        return [Node(next_state, self, action,
                     problem.path_cost(self.path_cost, self.state, action, next_state))
                for (action, next_state) in problem.successor(self.state)]


def tree_search(problem, fringe):
    fringe.append(Node(problem.initial)) #Mette nella coda la radice dell'albero (il nodo associato allo stato iniziale)
    max_depth = 0
    while fringe:
        node = fringe.pop()
        # Print some information about search progress
        if node.depth > max_depth:
            max_depth = node.depth # se depth del nodo è maggiore della max_depth, imposta questa come max_depth
            if max_depth < 50 or max_depth % 1000 == 0:
                pid = os.getpid()
                py = psutil.Process(pid)
                memoryUse = py.memory_info()[0] / 1024 / 1024
                print('Reached depth', max_depth,
                      'Open len', len(fringe),
                      'Memory used (MBytes)', memoryUse)

        if problem.goal_test(node.state):
            return node
        fringe.extend(node.expand(problem))
    return None

def breadth_first_tree_search(problem):
    "Search the shallowest nodes in the search tree first. [p 74]"
    return tree_search(problem, FIFOQueue())


def depth_first_tree_search(problem):
    "Search the deepest nodes in the search tree first. [p 74]"
    return tree_search(problem, Stack())