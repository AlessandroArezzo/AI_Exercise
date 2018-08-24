import math,bisect
import random
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
        update(self, A=[], order=order, f=f)
    def append(self, item):
        bisect.insort(self.A, (self.f(item), item))
    def __len__(self):
        return len(self.A)
    def pop(self):
        if self.order == min:
            return self.A.pop(0)[1]
        else:
            return self.A.pop()[1]


def memoize(fn, slot=None):
    if slot:
        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val
    else:
        def memoized_fn(*args):
            if not memoized_fn.cache.has_key(args):
                memoized_fn.cache[args] = fn(*args)
            return memoized_fn.cache[args]
        memoized_fn.cache = {}
    return memoized_fn



def calculateStartPoint(vertices):
    return searchPointByX(vertices,searchMinX(vertices))

def calculateGoalPoint(vertices):
    return searchPointByX(vertices,searchMaxX(vertices))

def searchMinX(vertices):
    minX=1000;
    for v in vertices:
        if(minX>v[0]):
            minX=v[0]
    return minX

def searchMinY(vertices):
    minY=1000;
    for v in vertices:
        if(minY>v[1]):
            minY=v[1]
    return minY

def searchMaxX(vertices):
    maxX=-1000;
    for v in vertices:
        if(maxX<v[0]):
            maxX=v[0]
    return maxX

def searchMaxY(vertices):
    maxY=-1000;
    for v in vertices:
        if(maxY<v[1]):
            maxY=v[1]
    return maxY

def searchPointByX(vertices,x):
    for v in vertices:
        if(v[0]==x):
            return v
    return -1


def getNeighbours(x,y,vor):
    result=[]
    for v in vor.ridge_vertices:
        tmpX=vor.vertices[v,0]
        tmpY=vor.vertices[v,1]
        for i in range(0,tmpX.__len__()):
            if(x==tmpX[i] and y==tmpY[i]):
                for j in range(0,tmpX.__len__()):
                    if((tmpX[j]!=x or tmpY[j]!=y) and controlArrayElement(tmpX[j],tmpY[j],result)==False):
                        result.append((tmpX[j],tmpY[j]))
                break
    return result


def controlArrayElement(x,y,array):
    for element in array:
        if(element[0]==x and element[1]==y):
            return True
    return False

def createMatrix(vor):
    matrix=[]
    for v in vor.vertices:
        arrayNeighbours=[v]
        arrayNeighbours.append(getNeighbours(v[0],v[1],vor))
        matrix.append(arrayNeighbours)
    return matrix


def update(x, **entries):
    """Update a dict; or an object with slots; according to entries.
    >>> update({'a': 1}, a=10, b=20)
    {'a': 10, 'b': 20}
    >>> update(Struct(a=1), a=10, b=20)
    Struct(a=10, b=20)
    """
    if isinstance(x, dict):
        x.update(entries)
    else:
        x.__dict__.update(entries)
    return x


def searchPoint(array,points):
    for p in array:
        if p==points:
            return True
    return False


def printResult(matrix,result,algoritmo,points,initialPoint,goalPoint):
    for region in matrix:
        for i in range(1, region.__len__()):
            plt.plot([region[0][0], region[i][0]], [region[0][1], region[i][1]], 'black',linewidth=0.3 )

    plt.xlim(searchMinX(points)-1, searchMaxX(points)+1)
    plt.ylim(searchMinY(points)-1, searchMaxY(points)+1)
    plt.plot(initialPoint[0], initialPoint[1], 'bp', markersize=14)
    plt.plot(goalPoint[0], goalPoint[1], 'rp', markersize=14)

    plt.title(algoritmo+"--COST:")
    plt.draw()
    plt.show(block=False)
    plt.pause(1)
    for node in reversed(result):
        plt.title(algoritmo+"--COST: "+unicode(node.path_cost))
        print node
        if (node.parent):
            plt.plot([node.parent.state.x, node.state.x], [node.parent.state.y, node.state.y], '-r',linewidth=2)
            plt.pause(1.5)
    plt.close()

def createGridActions(points):
    result=[]
    for p in points:
        tmp=[]
        tmpPoint1 = None
        tmpPoint2 = None
        distanceMin1 = 10000
        distanceMin2 = 10000
        distancePoints = 0
        tmp.append((p))
        for point in points:
            if(point is not p):
                distancePoints=distance(p,point)
                if(distancePoints<distanceMin1):
                    distanceMin1=distancePoints
                    tmpPoint1=point
                elif (distancePoints < distanceMin2):
                    distanceMin2 = distancePoints
                    tmpPoint2= point
        tmp.append(tmpPoint1)
        tmp.append(tmpPoint2)
        result.append(tmp)

    i=0
    for r in result:
        for p in range(1,len(r)):
            i=searchPointInMatrix(result,r[0],r[p])
            if(i is not -1):
                result[i].append(r[0])
    return result

def searchPointInMatrix(array,point1,point2):
    for i in range(0,len(array)):
        if(array[i][0]==point2):
            for p in array[i]:
                if(p==point1):
                    return -1
            return i
    return -1

def generateRandomPoints(num,min=0,max=10):
    i=1
    result=[]
    while(i<num):
        tmp=(random.randint(min,max),random.randint(min,max))
        if(not searchPoint(result,tmp)):
            result.append(tmp)
            i+=1
    return result

def searchInitialPoint(points):
    minX=10000
    point=None
    for p in points:
        if(p[0]<minX):
            minX=p[0]
            point=p
    return point

def searchGoalPoint(points):
    maxX=0
    point=None
    for p in points:
        if(p[0]>maxX):
            maxX=p[0]
            point=p
    return point

def createGrid(points,vertices):
    result=[]
    for i in range(0,len(points)):
        tmp=[]
        tmp.append(points[i])
        result.append(tmp)
    for v in vertices:
        for j in v:
            for z in v:
                if  j!=z and (not searchPoint(result[j],points[z])):
                    result[j].append(points[z])
    return result