import heapq
import sys

class edge:
    def __init__(self, weight, start, target):
        self.weight = weight
        self.start = start
        self.target = target

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacent = []
        self.minDist = sys.maxsize
    
    def __cmp__(self,other):
        return self.cmp(self.minDist, other.minDist)

    def __it__(self, other):
        selfPriority = self.minDist
        otherPriority = self.minDist
        return selfPriority < otherPriority
