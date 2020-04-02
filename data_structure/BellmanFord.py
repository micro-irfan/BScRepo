from collections import defaultdict

class Edge():
	def __init__(self,data=None):
		self.edge=data
		self.to=None
		self.cost=None 

class Bellman():
	def __init__(self):
		self.graph = defaultdict(list)
		self.edges = 0
		self.vertices = 0
		self.INF = ((63**1) - 1)//2
		self.Dlst = [self.INF] * self.vertices  #Tracks best distance from S to each Node
		self.graphEdges = []

	def addEdges(self, u, v, cost):
		self.graph[u].append((v,cost))

	def createEdges(self):
		tempLst = []
		for i in range(len(self.graph)):
			for key, value in self.graph.items():
				
				if key not in tempLst:
					tempLst.append(key)

				for a in value:
					edge = Edge()
					edge.edge = key
					edge.to = a[0]
					if a[0] not in tempLst:
						tempLst.append(a[0])
					edge.cost = a[1]
					
					self.graphEdges.append(edge)

		self.vertices = len(tempLst)
		self.Dlst = [self.INF] * self.vertices

	def BF(self, s):
		self.createEdges()
		self.Dlst[s] = 0
		n_inf = float("-inf")

		for i in range(len(self.Dlst) - 1):
			for edge in self.graphEdges:
				## Relax edge (Update D with shorter path)
				if self.Dlst[edge.edge] + edge.cost < self.Dlst[edge.to]:
					self.Dlst[edge.to] = self.Dlst[edge.edge] + edge.cost 
					
		for i in range(len(self.Dlst) - 1): 
			for edge in self.graphEdges:
				if self.Dlst[edge.edge] + edge.cost < self.Dlst[edge.to]:
					self.Dlst[edge.to] = n_inf

		print (self.Dlst)

g = Bellman()
g.addEdges(0, 1, 1)
g.addEdges(1, 2, 1)
g.addEdges(2, 4, 1)
g.addEdges(4, 3, -3)
g.addEdges(3, 2, 1)
g.addEdges(1, 5, 4)
g.addEdges(1, 6, 4)
g.addEdges(5, 6, 5)

g.addEdges(6, 7, 4)
g.addEdges(5, 7, 3)	
g.BF(0)
