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

class Dijkstra:
    def CalculateShortestPath(self, vertexList, start):
        q=[]
        start.minDist = 0
        heapq.heappush(q, start)

        while len(q)>0:
            node = heapq.heappop(q)
            for edge in node.adjacent:
                u = edge.start
                v = edge.target
                newDist = u.minDist + edge.weight

                if newDist < v.minDist:
                    v.predecessor = u
                    v.minDist = newDist
                    heapq.heappush(q,v)

    def GetShortestPath(self, target):
        print("shortest path to vertex is", target.minDist)
        node = target
        while node is not None:
            print(node.name)
            node = node.predecessor

