from collections import defaultdict
import heapq

class Edge():
	def __init__(self, elem):
		self.from_ = elem
		self.to = None
		self.cost = None

	def __lt__(self, other):
		return self.cost < other.cost

class Prims():
	def __init__(self):
		self.N = 0
		self.PQ = []
		self.graph = defaultdict(list)
		self.visited = []

	def addEdges(self,u,v,cost):
		self.graph[u].append((v, cost))
		self.graph[v].append((u, cost))

	def GenerateN(self):
		tmplst = []
		for key, values in self.graph.items():
			if key not in tmplst:
				tmplst.append(key)
				for a in values:
					if a[0] not in tmplst:
						tmplst.append(a[0])

		self.N = len(tmplst)

	def lazyPrims(self, s = 0):
		self.GenerateN()
		self.visited = [False] * self.N

		m = self.N - 1
		edgecount, mstCost = 0, 0
		mstEdges = [None] * m
		self.addEdgesToPQ(s)

		while len(self.PQ) != 0 and edgecount != m:
			edge = heapq.heappop(self.PQ)
			nodeIndex = edge.to

			if self.visited[nodeIndex]:
				continue

			mstEdges[edgecount] = edge
			edgecount += 1
			mstCost += edge.cost
			self.addEdgesToPQ(nodeIndex)

		if edgecount != m:
			return (None, None)

		return (mstCost, mstEdges)

	def addEdgesToPQ(self, nodeIndex):
		self.visited[nodeIndex] = True
		edges = self.graph.get(nodeIndex)
		if edges:
			for edge in edges:
				edge1 = Edge(nodeIndex)
				edge1.to, edge1.cost = edge[0], edge[1] 
				if not self.visited[edge1.to]:
					heapq.heappush(self.PQ, edge1) 	

	def printFinalAnswer(self):
		cost, edges = self.lazyPrims()
		if cost is None:
			print ("MST does not exist")
		else:
			print ("MST cost: " + str(cost))
			for a in edges:
				print ("From {} to {} that cost: {}".format(a.from_, a.to, a.cost))

g = Prims()
'''
g.addEdges(0, 1, 5)
g.addEdges(1, 2, 4)
g.addEdges(2, 9, 2)
g.addEdges(0, 4, 1)
g.addEdges(0, 3, 4)
g.addEdges(1, 3, 2)
g.addEdges(2, 7, 4)
g.addEdges(2, 8, 1)
g.addEdges(9, 8, 0)
g.addEdges(4, 5, 1)
g.addEdges(5, 6, 7)
g.addEdges(6, 8, 4)
g.addEdges(4, 3, 2)
g.addEdges(5, 3, 5)
g.addEdges(3, 6, 11)
g.addEdges(6, 7, 1)
g.addEdges(3, 7, 2)
g.addEdges(7, 8, 6)

MST cost: 14
From 0 to 4 that cost: 1
From 4 to 5 that cost: 1
From 4 to 3 that cost: 2
From 3 to 1 that cost: 2
From 3 to 7 that cost: 2
From 7 to 6 that cost: 1
From 7 to 2 that cost: 4
From 2 to 8 that cost: 1
From 8 to 9 that cost: 0
'''
'''
g.addEdges(1, 2, 4)
g.addEdges(0, 3, 3)
g.addEdges(0, 1, 6)
g.addEdges(3, 6, 8)
g.addEdges(4, 5, 7)
g.addEdges(4, 7, 9)
g.addEdges(5, 8, 10)
g.addEdges(6, 7, 11)
g.addEdges(7, 8, 5)
g.addEdges(1, 4, 2)
g.addEdges(2, 5, 12)
g.addEdges(3, 4, 1)
'''

g.addEdges(0, 1, 10)
g.addEdges(0, 2, 1)
g.addEdges(0, 3, 4)
g.addEdges(1, 4, 0)
g.addEdges(1, 2, 3)
g.addEdges(2, 5, 8)
g.addEdges(2, 3, 2)
g.addEdges(3, 5, 2)
g.addEdges(3, 6, 7)
g.addEdges(4, 5, 1)
g.addEdges(4, 7, 8)
g.addEdges(5, 6, 6)
g.addEdges(6, 7, 12)

'''
From Slides
MST cost: 20
From 0 to 2 that cost: 1
From 2 to 3 that cost: 2
From 3 to 5 that cost: 2
From 5 to 4 that cost: 1
From 4 to 1 that cost: 0
From 5 to 6 that cost: 6
From 4 to 7 that cost: 8
'''

print (g.printFinalAnswer())