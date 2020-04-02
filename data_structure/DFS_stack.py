# Python program to print DFS traversal for complete graph 
from collections import defaultdict 
from stack import Stack
  
# This class represents a directed graph using adjacency 
# list representation 
class Graph: 
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v)

    def numberofNodes(self, graph):
        lst = []
        for key, value in graph.items():
            if key not in lst:
                lst.append(key)
            if value not in lst:
                lst.append(value)

        return len(lst) 

    def DFSStack(self, start):
        V = len(self.graph)  #total vertices 
        number = self.numberofNodes(self.graph)
        # Mark all the vertices as not visited 
        visited = [False] * number
        count = 0
        stack = Stack(number)
        stack.push(start)
        lstofNodes = []
        while stack.is_empty() == False:
            DFScount = 0
            node = stack.pop()
            lstofNodes.append(node)
            #print ('Count at Current Node {1} : {0}'.format(count, node))

            if not visited[node]:
                count += 1 ## Count number of Nodes Visited
                visited[node]= True
                edges = self.graph.get(node)

                if edges != None:
                    for edge in edges:
                        if visited[edge] == False:
                            stack.push(edge)

        return lstofNodes
        print ('Total Count: ' + str(count)) 

g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 9) 
g.addEdge(1, 8) 
g.addEdge(9, 8) 
g.addEdge(8, 7) 
g.addEdge(7, 10)
g.addEdge(10, 10) 
g.addEdge(11, 11)
g.addEdge(7, 11) 
g.addEdge(7, 3) 
g.addEdge(7, 6) 
g.addEdge(6, 5) 
g.addEdge(3, 5) 
g.addEdge(3, 4)
g.addEdge(3, 2) 
g.addEdge(12, 12)

print ("Following is Depth First Traversal")
print (g.DFSStack(0)) 
