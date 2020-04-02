from collections import defaultdict

class Bridges():
	def __init__(self):
		self.id = 0
		self.graph = defaultdict(list)
		self.N = 0
		self.visited = []
		self.ids = []
		self.low = []
		self.bridges = []
		self.outEdgeCount = 0
		self.isArt = []

	def addEdges(self, u, v): #u = to , v = from
		self.graph[u].append(v)

	def findN(self):
		tmplst = []
		for key, values in self.graph.items():
			if key not in tmplst:
				tmplst.append(key)
			for a in values:
				if a not in tmplst:
					tmplst.append(a)
		self.N = len(tmplst)

	def printValues(self):
		for a in self.bridges:
			print ('Bridges between Node: {} and {}'.format(a[0], a[1]))

	def printArticulationPoints(self):
		print (self.isArt)

	def findBridges(self):
		self.findN()
		self.ids = [0] * self.N
		self.low = [0] * self.N
		self.visited  = [False] * self.N
		self.isArt = [False] * self.N

		bridges = []
		for i in range(self.N):
			if not self.visited[i]:
				self.outEdgeCount = 0
				self.dfs(i, i, -1)
				if self.outEdgeCount > 1:
					self.isArt[i] = self.outEdgeCount

		print (self.low)
		return self.bridges

	def dfs(self,root, at, parent):
		if parent == root:
			self.outEdgeCount += 1
		self.visited[at] = True
		self.low[at] = self.id
		self.ids[at] = self.id
		self.id += 1

		To = self.graph.get(at)
		if To:
			for a in To:
				if a == parent:
					continue
				if not self.visited[a]:
					self.dfs(root, a, at)
					self.low[at] = min(self.low[at], self.low[a])
					#Articulation point found via a bridge
					if (self.ids[at] < self.low[a]):
						self.isArt[at] = True
						self.bridges.append([at, a])
					#Articulation point found via a cycle
					if (self.ids[at] == self.low[a]):
						self.isArt[at] = True
				else:
					self.low[at] = min(self.low[at], self.ids[a])

g = Bridges()

g.addEdges(0,1)
g.addEdges(2,0)
g.addEdges(1,2)
g.addEdges(2,3)
g.addEdges(3,4)
g.addEdges(2,5)
g.addEdges(5,6)
g.addEdges(6,7)
g.addEdges(7,8)
g.addEdges(8,5)
#g.addEdges(8,2)

g.findBridges()
g.printValues()
g.printArticulationPoints()
