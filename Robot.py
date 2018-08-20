from search import Problem
from copy import deepcopy
import utils


class Robot(Problem):

    """Nell'esempio del Puzzle si crea la configurazione iniziale attraverso un metodo make_initial_state che
     crea una configurazione random del problema. In tal caso andrebbe creato allo stesso modo il nodo del goal
     (nel puzzle non crea uno stato per il goal, configurazione statica).
     In questa implementazione si suppone di avere come descrizione del problema una tessellationGrid
     del tipo: [[(ptoX),(vicino n1 del ptoX),(vicino n2 del ptoX)...],[...()...],...]"""

    def __init__(self,initialPoint,goalPoint,tessellationGrid):
        self.initial=RobotState(initialPoint)
        self.goal=RobotState(goalPoint)
        self.grid=tessellationGrid
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
        actions=[]
        for point in self.grid:
            if(point[0]==(state.x,state.y)):
                for i in range(1,point.__len__()):
                    actions.append(point[i])
                return actions
        return None

    def path_cost(self, c, state1, action, state2):
        return c+utils.distance((state1.x,state1.y),(state2.x,state2.y))

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
        return utils.distance((self.x,self.y),(goal.x,goal.y))



