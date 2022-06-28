from Graph import Graph

def getAdjList(graph, key):
    myList = []
    for k in graph.adjList:
        if k == key:
            return graph.adjList[k]

vertices = ['A', 'B', 'C', 'D', 'E']

g = Graph()

for v in vertices:
    g.addVertex(v)

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('A', 'D')
g.addEdge('A', 'E')
g.addEdge('B', 'D')
g.addEdge('C', 'E')
g.addEdge('E', 'D')
g.print()
print(getAdjList(g, 'A'))