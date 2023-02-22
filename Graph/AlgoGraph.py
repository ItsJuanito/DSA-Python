from Graph import Graph
import sys
sys.path.append('..')
from Queue.Queue import Queue
from Stack.Stack import Stack

def hasPath(graph, key, dst):
    queue = Queue()
    queue.enqueue(key)
    while queue.size() > 0:
        current = queue.dequeue()
        if current == dst:
            return True
        for values in graph[current]:
            queue.enqueue(values)
    return False

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

if __name__ == "__main__":
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
    print(g.getNeighbors('A'))

    print("Has Path : " + str(hasPath(graph, 'A', 'E')))

    print("Depth first search: ")
    depthFirstSearch(graph, 'A')

    print("\nBreadth first search: ")
    breadthFirstSearch(graph, 'A')

'''
Sample Outputs:
 - A -> B C 
 - B -> A D 
 - C -> A E 
 - D -> B F 
 - E -> C 
 - F -> D 
 - ['B', 'C']
 - Has Path: True
 - Depth first search: 
 - A C E B D F 
 - Breadth first search: 
 - A B C D E F 
  
Graph Structure:
{
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : [],
    'F' : []
}

Graph Representation:
    A -> B -> D -> F 
     \ 
      -> C -> E   

'''