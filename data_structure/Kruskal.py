from collections import defaultdict
from unionfind import UnionFind
import heapq

class Edge():
	def __init__(self, elem):
		self.u = elem
		self.v = None
		self.cost = None

	def __lt__(self, other):
		return self.cost < other.cost

class Kruskal():
	def __init__(self):
		self.graph = defaultdict(list)
		self.N = 0
		self.PQ = []
		self.mstCost = 0
		self.mst = []

	def addEdges(self, u, v, cost):
		self.graph[u].append((v, cost))
		self.edge = Edge(u)
		self.edge.v = v
		self.edge.cost = cost
		heapq.heappush(self.PQ, self.edge)

	def generatePQ(self):
		tmplst = []
		for key, value in self.graph.items():
			if key not in tmplst:
				tmplst.append(key)
			for a in value:
				if a[0] not in tmplst:
					tmplst.append(a[0])	
		self.N = len(tmplst)

	def printValues(self):
		for a in self.PQ:
			print (a.u, a.v, a.cost)

	def kruskalMST(self):
		self.generatePQ()
		uf = UnionFind()
		uf.WeightedQuickUnionUF(self.N)
		self.mst = [None] * self.N 

		index = 0

		while len(self.PQ) != 0:
			edge = heapq.heappop(self.PQ)
			if (uf.connected(edge.u, edge.v)):
				continue
			uf.unify(edge.v, edge.u)
			self.mstCost += edge.cost
			self.mst[index] = edge
			index += 1
			if uf.size1(0) == self.N:
				break

		mstExists = (uf.size1(0) == self.N)
		solved = True

		if solved:
			return self.mstCost
		else:
			return None

	def printAnswer(self):
		if self.mstCost == None:
			print ("MST does not exist")
		else:
			print ("MST cost: ", self.mstCost)
			for a in self.mst:
				if a:
					print ("Used edge ({},{}) with cost: {}".format(a.u,a.v,a.cost))





g = Kruskal()

g.addEdges(0,7,0.16)
g.addEdges(2,3,0.17)		
g.addEdges(1,7,0.19)	
g.addEdges(0,2,0.26)	
g.addEdges(5,7,0.28)	
g.addEdges(4,5,0.35)	
g.addEdges(6,2,0.40)	
g.kruskalMST()
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
#g.printValues()
(g.kruskalMST())
'''

g.printAnswer()
