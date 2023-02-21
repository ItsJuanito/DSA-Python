class Graph:
    
    def __init__(self):
        self.adjList = {}
    
    def addVertex(self, v):
        self.adjList[v] = []
    
    def addEdge(self, v, w):
        self.adjList.get(v).append(w)
        self.adjList.get(w).append(v)

    def deleteVertex(self, v):
        for keys in self.adjList:
            for values in self.adjList[keys]:
                if values == v:
                    self.adjList.get(keys).remove(v)
        if v in self.adjList:
            self.adjList.pop(v)
    
    def getNeighbors(self, k):
        for key, values in self.adjList.items():
            if key == k and values:
                return list(values)
        else:
            return 'There are no neighbors'

    def print(self):
        string = ""
        for k in self.adjList.keys():
            string = ""
            for i in self.adjList[k]:
                string += i + " "
            print(k + " -> " + string)

if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D']
    g = Graph()
    for v in vertices:
        g.addVertex(v)
    g.addEdge('A', 'B')
    g.addEdge('A', 'C')
    g.addEdge('B', 'D')
    g.addEdge('D', 'C')
    g.print()
    g.deleteVertex('D')
    print("After removing 'D': ")
    g.print()
    neighbors = g.getNeighbors('A')
    print(neighbors)