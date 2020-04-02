from collections import defaultdict

class TopoSort():
	def __init__(self):
		self.graph = defaultdict(list)

	def add(self, u, v, cost):
		self.graph[u].append(v)

	def NumberOfNodes(self, graph):
		lst = []
		for key, value in graph.items():
			if key not in lst:
				lst.append(key)
			for a in value:
				if a not in lst:
					lst.append(a)
		return len(lst) 

	def getGraph(self):
		print (self.graph) 
		print (self.NumberOfNodes(self.graph))

	def topSort(self):
		N = self.NumberOfNodes(self.graph)
		V = [False] * N
		ordering = [0] * N
		i = N - 1

		for at in range(0, N):
			if V[at] == False:
				self.dfs(i, at, V, ordering)

		return ordering

	def dfs(self, i, at, V, ordering):
		V[at] = True
		edges = self.graph.get(at)
		if edges:
			for edge in edges:
				if V[edge] == False:
					i = self.dfs(i, edge, V, ordering)

		ordering[i] = at
		return i-1

g = TopoSort()
g.add(0, 1, 3);
g.add(0, 2, 2);
g.add(0, 5, 3);
g.add(1, 3, 1);
g.add(1, 2, 6);
g.add(2, 3, 1);
g.add(2, 4, 10);
g.add(3, 4, 5);
g.add(5, 4, 7);

g.getGraph()
print (g.topSort())