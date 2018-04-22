from search import Problem
from copy import deepcopy
import utils

class Robot(Problem):

    def __init__(self,initialX,initialY,goalX,goalY,tessellationGrid):
        self.initial=RobotState(initialX,initialY)
        self.goal=RobotState(goalX,goalY)
        self.grid=tessellationGrid
        print("Start problem")
        print self.initial


    def successor(self, state):
        for action in self.getActions(state.x,state.y):
            nexts = state.move(action)
            if nexts is not None:
                yield (action,nexts)

    def goal_test(self, state):
        return state.x==self.goal.x and state.y==self.goal.y

    def getActions(self,x,y):
        """TODO: da capire come fare ad ottenere i vettori direzione a partire dal punto del piano x,y ed alla grid stessa"""

    def path_cost(self, c, state1, action, state2):
        return c+utils.distance((state1.x,state1.y),(state2.x,state2.y))

class RobotState:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return "Il robot si trova nello stato ("+unicode(self.x)+","+unicode(self.y)+")"

    def move(self,direction):
        """ TODO: da capire come portare il robot nella nuova posizione a partire dalla direcrion che conterrà il vettore 
         restituito dal metodo getActions di Robot"""
        ch=deepcopy(self)
        ch.x = direction[0]
        ch.y=direction[1]
        return ch



