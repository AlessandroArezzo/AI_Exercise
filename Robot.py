from search import Problem
from copy import deepcopy
from utils import distance


class Robot(Problem):

    """L'attributo dict e' un dizionario che associa ad ogni punto del piano un array contenente tutti i punti ad esso adiacenti"""
    def __init__(self,initialPoint,goalPoint,dict):
        self.initial=RobotState(initialPoint)
        self.goal=RobotState(goalPoint)
        self.dictActions=dict
        print("Start problem")
        print self.initial

    def successor(self, state):
        result=[]
        actions=self.getActions(state)
        for action in actions:
            nexts = state.move(action)
            if nexts is not None:
                result.append((action,nexts))
        return result

    def goal_test(self, state):
        return state.x==self.goal.x and state.y==self.goal.y


    def getActions(self,state):
        """Ricerca nel dizionario il punto corrispondente allo stato state e vi ritorna l'array ad esso associato"""
        return self.dictActions[(state.x,state.y)]

    def path_cost(self, c, state1, action, state2):
        return c+distance((state1.x,state1.y),(state2.x,state2.y))

    def h(self,node):
        return node.state.h(self.goal)

class RobotState:
    def __init__(self,point):
        self.x=point[0]
        self.y=point[1]

    def __str__(self):
        return "STATO: ("+unicode(self.x)+","+unicode(self.y)+")"

    def move(self,point):
        ch=deepcopy(self)
        ch.x = point[0]
        ch.y=point[1]
        return ch

    def h(self,goal):
        """Come euristica si usa la distanza in linea d'area tra lo stato ed il goal"""
        return distance((self.x,self.y),(goal.x,goal.y))



