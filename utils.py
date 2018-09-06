import math,bisect,random
from matplotlib import pyplot as plt
def distance((ax, ay), (bx, by)):
    return math.hypot((ax - bx), (ay - by))

class Queue:
    def __init__(self):
        pass #abstract

    def extend(self, items):
        for item in items: self.append(item)

def Stack():
    return []

class FIFOQueue(Queue):
    def __init__(self):
        self.A = [];
        self.start = 0
    def append(self, item):
        self.A.append(item)
    def __len__(self):
        return len(self.A) - self.start
    def extend(self, items):
        self.A.extend(items)
    def pop(self):
        e = self.A[self.start]
        self.start += 1
        return e

class PriorityQueue(Queue):
    def __init__(self, order=min, f=lambda x: x):
         self.A=[]
         self.order=order
         self.f=f
    def append(self, item):
        bisect.insort(self.A, (self.f(item), item))
    def __len__(self):
        return len(self.A)
    def pop(self):
        if self.order == min:
            return self.A.pop(0)[1]
        else:
            return self.A.pop()[1]


#Metodi atti alla corretta visualizzazione del piano, garantiscono di visualizzare il piano con i giusti limiti
def searchMinX(vertices):
    minX=1000
    for v in vertices:
        if(minX>v[0]):
            minX=v[0]
    return minX

def searchMinY(vertices):
    minY=1000
    for v in vertices:
        if(minY>v[1]):
            minY=v[1]
    return minY

def searchMaxX(vertices):
    maxX=-1000
    for v in vertices:
        if(maxX<v[0]):
            maxX=v[0]
    return maxX

def searchMaxY(vertices):
    maxY=-1000
    for v in vertices:
        if(maxY<v[1]):
            maxY=v[1]
    return maxY


def searchPoint(array,points):
    for p in array:
        if p==points:
            return True
    return False


def printResult(dictlines,result,algoritmo,points,problem):
    fig=plt.figure()
    for point in dictlines:
        for neighbour in dictlines[point]:
            plt.plot([point[0], neighbour[0]], [point[1], neighbour[1]], 'black',linewidth=0.3 )

    plt.xlim(searchMinX(points)-10, searchMaxX(points)+ 10)
    plt.ylim(searchMinY(points)-10, searchMaxY(points)+10)
    plt.plot(problem.initial.x, problem.initial.y, 'bp', markersize=14)
    plt.plot(problem.goal.x, problem.goal.y, 'rp', markersize=14)

    plt.title(algoritmo+"--COST: --N.PASSI")
    plt.show(block=False)
    plt.pause(1)
    i=0 # variabile utile per stampare il numero di passi compiuti dal robot
    for node in reversed(result):
        print node
        print "--Cost: "+unicode(node.path_cost)+"--#STEPS: "+unicode(i)
        if(plt.fignum_exists(fig.number)):
            plt.title(algoritmo+"--COST: "+unicode(node.path_cost)+"--#STEPS:"+unicode(i))
            if (node.parent):
                plt.plot([node.parent.state.x, node.state.x], [node.parent.state.y, node.state.y], '-r',linewidth=2)
                plt.pause(1.5)
            i+=1
        else:
            break
    plt.close()

def generateRandomPoints(num,min=0,max=10):
    i=1
    result=[]
    while(i<num+1):
        tmp=(random.randint(min,max),random.randint(min,max))
        if(not searchPoint(result,tmp)):
            result.append(tmp)
            i+=1
    return result

#Come goal si sceglie il punto avente coordinata x minore
def searchInitialPoint(points):
    minX=10000
    point=None
    for p in points:
        if(p[0]<minX):
            minX=p[0]
            point=p
    return point

#Come goal si sceglie il punto avente coordinata x maggiore
def searchGoalPoint(points):
    maxX=-10000
    point=None
    for p in points:
        if(p[0]>maxX):
            maxX=p[0]
            point=p
    return point

def createDict(points,delauneyObject):
    dict={}
    for v in delauneyObject.vertices:
        for j in v:
            serial = points[j]
            if serial not in dict:
                dict[serial]=[]
            for z in v:
                if(z!=j and (not searchPoint(dict[serial],points[z]))):
                    dict[serial].append(points[z])
    return dict

