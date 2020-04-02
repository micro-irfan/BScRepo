#Strongly Connected Points
from collections import defaultdict
from stack import Stack

class Tarjan():
	def __init__(self):
		self.graph = defaultdict(list)
		self.N = 0
		self.unvisited = -1
		self.id = 0
		self.sccCount = 0
		self.ids = []
		self.low = []
		self.onStack = []
		self.stack = Stack(self.N)

	def calculateN(self):
		tmplst = []
		for key,value in self.graph.items():
			if key not in tmplst:
				tmplst.append(key)
			for a in value:
				if a not in tmplst:
					tmplst.append(a)

		self.N = len(tmplst)

	def addEdges(self, u, v):
		self.graph[u].append(v)

	def findSCCs(self):
		self.calculateN()
		self.ids = [0] * self.N
		self.low = [0] * self.N
		self.onStack = [False] * self.N
		self.stack = Stack(self.N)

		for i in range(self.N):
			self.ids[i]	= self.unvisited
		for i in range(self.N):
			if self.ids[i] == self.unvisited:
				self.dfs(i)

		return self.low

	def dfs(self, at):
		self.stack.push(at)
		self.onStack[at] = True
		self.low[at] = self.id
		self.ids[at] = self.id
		self.id += 1

		To = self.graph.get(at)
		if To:
			for a in To:
				if self.ids[a] == self.unvisited:
					self.dfs(a)
				if self.onStack[a]:
					self.low[at] = min(self.low[at], self.low[a])
 		
		if (self.ids[at] == self.low[at]):
			while not self.stack.is_empty():
				node = self.stack.pop()
				self.onStack[node] = False
				self.low[node] = self.ids[at]
				if node == at:
					break
			self.sccCount += 1

	def printAnswers(self):
		print ("Number of Strongly Connected Components: {}".format(self.sccCount))
		final = defaultdict(list)
		for a in range(len(self.low)):
			final[self.low[a]].append(a) 
		for key, values in final.items():
			print ("Nodes : {} are strongly connected Components!".format(values))


g = Tarjan()
g.addEdges(6,0)
g.addEdges(6,2)
g.addEdges(3,4)
g.addEdges(6,4)
g.addEdges(2,0)
g.addEdges(0,1)
g.addEdges(4,5)
g.addEdges(5,6)
g.addEdges(3,7)
g.addEdges(7,5)
g.addEdges(1,2)
g.addEdges(7,3)
g.addEdges(5,0)

print (g.findSCCs())
g.printAnswers()