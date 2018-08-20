import math,bisect
import random
import numpy as np
from matplotlib import pyplot as plt
from Queue import PriorityQueue


def distance((ax, ay), (bx, by)):
    "The distance between two (x, y) points."
    return math.hypot((ax - bx), (ay - by))



class Queue:
    """Queue is an abstract class/interface. There are three types:
        Stack(): A Last In First Out Queue.
        FIFOQueue(): A First In First Out Queue.
        PriorityQueue(lt): Queue where items are sorted by lt, (default <).
    Each type supports the following methods and functions:
        q.append(item)  -- add an item to the queue
        q.extend(items) -- equivalent to: for item in items: q.append(item)
        q.pop()         -- return the top item from the queue
        len(q)          -- number of items in q (also q.__len())
    Note that isinstance(Stack(), Queue) is false, because we implement stacks
    as lists.  If Python ever gets interfaces, Queue will be an interface."""

    def __init__(self):
        pass #abstract

    def extend(self, items):
        for item in items: self.append(item)

def Stack():
    """Return an empty list, suitable as a Last-In-First-Out Queue."""
    return []

class FIFOQueue(Queue):
    """A First-In-First-Out Queue."""
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
        if self.start > 5 and self.start > len(self.A)/2:
            self.A = self.A[self.start]
            self.start = 0
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
    """Memoize fn: make it remember the computed value for any argument list.
    If slot is specified, store result in that slot of first argument.
    If slot is false, store results in a dictionary."""
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


def createPlot(points):
    result=[]
    tmp=[]
    for i in range(0,len(points)):
        tmp=[]
        tmp.append(points[i])
        ran=i
        ran2=i
        while(ran==i or ran2==i or ran==ran2 or searchPoint(result,ran)):
            ran=random.randint(0,points.__len__()-1)
            ran2=random.randint(0,points.__len__()-1)
        tmp.append(points[ran])
        tmp.append(points[ran2])
        result.append(tmp)
    return result

def searchPoint(array,points):
    for p in array:
        if p[0]==points:
            return True
    return False
