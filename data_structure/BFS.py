from collections import defaultdict 

class Graph: 
	def __init__(self): 
        # default dictionary to store graph 
		self.graph = defaultdict(list)
  
    # function to add an edge to graph 
	def addDirectedEdge(self,u,v,weight): 
		self.graph[u].append(v)

	def numberofNodes(self, graph):
		lst = []
		for key, value in graph.items():
			if key not in lst:
				lst.append(key)
			if value not in lst:
				lst.append(value)

		return len(lst)

	def BFS(self, start):
		PQ = []
		PQ.append(start)
		V = len(self.graph)  #total vertices 
		number = self.numberofNodes(self.graph)
        # Mark all the vertices as not visited 
		visited = [False] * number
		prev = [None] * number 
		lstofNodes= []

		visited[start] = True
		while PQ:
			node = PQ.pop(0)
			lstofNodes.append(node)
			neighbors = self.graph.get(node)
			if neighbors:
				for i in neighbors:
					if not visited[i]:
						PQ.append(i)
						visited[i] = True
						prev[i] = node

		print (lstofNodes)
		return prev

	def reconstructPath(self, s, e, prev):
		path = []
		at = e
		while at != None:
			path.append(at)
			at = prev[at]
			
		path = path[::-1]

		if path[0] == s:
			return path
		return []

g = Graph() 
g.addDirectedEdge(1, 2, 1);
g.addDirectedEdge(1, 2, 1); # Double edge
g.addDirectedEdge(1, 3, 1);
g.addDirectedEdge(2, 4, 1);
g.addDirectedEdge(2, 5, 1);
g.addDirectedEdge(3, 6, 1);
g.addDirectedEdge(3, 7, 1);
g.addDirectedEdge(2, 2, 1); # Self loop
g.addDirectedEdge(2, 3, 1);
g.addDirectedEdge(6, 2, 1);
g.addDirectedEdge(1, 6, 1);

print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)") 
a = (g.BFS(1))
print (a)
b = g.reconstructPath(1,5,a)
print (b)
