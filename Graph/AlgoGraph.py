from Graph import Graph
import sys
sys.path.append('..')
from Queue.Queue import Queue
from Stack.Stack import Stack

def getAdjList(graph, key):
    for k in graph.adjList:
        if k == key:
            return graph.adjList[k]

def depthFirstSearch(graph, key):
    stack = Stack()
    stack.push(key)
    while stack.size() > 0:
        current = stack.pop()
        print(current, end=" ")
        for values in graph[current]:
            stack.push(values)

def breadthFirstSearch(graph, key):
    queue = Queue()
    queue.enqueue(key)
    while queue.size() > 0:
        current = queue.dequeue()
        print(current, end=" ")
        for values in graph[current]:
            queue.enqueue(values)

graph = {
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : [],
    'F' : []
}

vertices = ['A', 'B', 'C', 'D', 'E', 'F']

g = Graph()

for v in vertices:
    g.addVertex(v)

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('C', 'E')
g.addEdge('D', 'F')
g.print()
print(getAdjList(g, 'A'))
print("Depth first search: ")
depthFirstSearch(graph, 'A')
print("\nBreadth first search: ")
breadthFirstSearch(graph, 'A')

'''
{
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : [],
    'F' : []
}
'''