import heapq

class Edge():
	def __init__(self, from_, to, capacity):
		self.from_ = from_ 
		self.to = to
		self.capacity = capacity
		self.flow = 0
		self.residual = None

	def isResidual(self):
		return self.capacity == 0

	def remainingCapacity(self):
		return (self.capacity - self.flow)

	def augment(self, bottleNeck):
		self.flow += bottleNeck
		self.residual.flow -= bottleNeck

	def __lt__(self, other):
		return self.from_ < other.from_	

	#n - no. of nodes in the graph including s and t
	#s - the index of source node
	#t - the index of sink node
class NetworkFlowSolverBase():
	def __init__(self, n, s, t):
		self.graph = [[] for _ in range(n)]
		self.visited = [0] * n
		self.visitedToken = 1
		self.maxflow = 0 
		self.solved = False
		self.n = n
		self.s = s
		self.t = t 

	def addEdge(self, u, v, capacity):
		if capacity <= 0:
			print ("Forward Edge capacity <= 0")
		e1 = Edge(u,v,capacity)
		e2 = Edge(v,u,0)
		e1.residual = e2
		e2.residual = e1
		self.graph[u].append(e1)
		self.graph[v].append(e2)

	def getGraph(self):
		self.execute()
		return self.graph

	def getMaxFlow(self):
		self.execute()
		self.toString()
		print ('Maximum flow from S to T is {0}.'.format(self.maxflow))
		return self.maxflow

	def execute(self):
		if self.solved:
			return
		self.solved = True
		self.solve()

	def solve(self):
		pass

	def markNodeAsUnvisited(self):
		self.visitedToken += 1

	def visited_(self, i):
		return self.visited[i] == self.visitedToken

	def visit(self, i):
		self.visited[i] = self.visitedToken

	def toString(self):
		for a in self.graph:
			for edge in a:
				print ('Edge from {1} -> {0} | flow = {2} | capacity = {3} | is residual: {4}'.format(edge.to, edge.from_, edge.flow, edge.capacity, edge.isResidual()) )


class EdmondsKarp(NetworkFlowSolverBase):
	def __init__(self,n,s,t):
		super().__init__(n,s,t)

	def solve(self):
		while True:
			self.markNodeAsUnvisited()
			flow = self.bfs()
			if flow == 0 or flow == None:
				break
			self.maxflow += flow

	def bfs(self):
		q = []
		self.visit(self.s)
		if len(q) != self.n:
			heapq.heappush(q, self.s)

		prev = [None] * self.n
		while len(q) != 0:
			node = heapq.heappop(q)
			if node == self.t:
				break

			edges = self.graph[node]
			for edge in edges:
				cap = edge.remainingCapacity()
				if cap > 0 and not self.visited_(edge.to):
					self.visit(edge.to)
					prev[edge.to] = edge
					if len(q) != self.n:
						heapq.heappush(q, edge.to)

		if prev[self.t] == None:
			return 0

		p_inf = float("inf")
		bottleNeck = p_inf
		edge = prev[self.t]
		while True:
			if edge == None:
				break
			bottleNeck = min(bottleNeck, edge.remainingCapacity())
			edge = prev[edge.from_]

		edge = prev[self.t]
		while True:
			if edge == None:
				break
			edge.augment(bottleNeck)
			edge = prev[edge.from_]	

		return bottleNeck

'''
n = 6;
s = n - 1;
t = n - 2;

solver = EdmondsKarp(n,s,t)

    #Source edges
solver.addEdge(s, 0, 10)
solver.addEdge(s, 1, 10)

   # Sink edges
solver.addEdge(2, t, 10)
solver.addEdge(3, t, 10)

   # Middle edges
solver.addEdge(0, 1, 2)
solver.addEdge(0, 2, 4)
solver.addEdge(0, 3, 8)
solver.addEdge(1, 3, 9)
solver.addEdge(3, 2, 6)

print (solver.getMaxFlow())
'''

n = 11	
s, t = n - 2, n - 1	
solver = EdmondsKarp(n,s,t)

solver.addEdge(s, 0, 5);
solver.addEdge(s, 1, 10);
solver.addEdge(s, 2, 5);

solver.addEdge(0, 3, 10);
solver.addEdge(1, 0, 15);
solver.addEdge(1, 4, 20);
solver.addEdge(2, 5, 10);
solver.addEdge(3, 4, 25);

solver.addEdge(3, 6, 10);
solver.addEdge(4, 2, 5);

solver.addEdge(4, 7, 30);
solver.addEdge(5, 7, 5);

solver.addEdge(5, 8, 10);
solver.addEdge(7, 3, 15);

solver.addEdge(7, 8, 5);

solver.addEdge(6, t, 5);
solver.addEdge(7, t, 15);
solver.addEdge(8, t, 10);

(solver.getMaxFlow())