from collections import defaultdict

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

	def toString(self):
		for a in self.graph:
			for edge in a:
				print ('Edge from {1} -> {0} | flow = {2} | capacity = {3} | is residual: {4}'.format(edge.to, edge.from_, edge.flow, edge.capacity, edge.isResidual()) )


class FordFulkerson(NetworkFlowSolverBase):
	def __init__(self, n, s, t):
		super().__init__(n,s,t)

	def solve(self):
		global p_inf
		p_inf = float("inf")

		while True:
			f = self.dfs(self.s, p_inf)
			if f == None or f == 0:
				break
			self.visitedToken += 1
			self.maxflow += f

	def dfs(self, node, flow):
		if node == self.t:
			return flow

		self.visited[node] = self.visitedToken

		edges = self.graph[node] 
		for edge in edges:
			if edge.remainingCapacity() > 0 and self.visited[edge.to] != self.visitedToken:					
				bottleNeck = self.dfs(edge.to, min(flow, edge.remainingCapacity()))
				if bottleNeck:
					if bottleNeck>0:
						edge.augment(bottleNeck)
						return bottleNeck


class EdmondsKarp(NetworkFlowSolverBase):
	def __init__(self,s,n,t):
		super().__init__(self,n,s,t)



'''
n = 12	
s, t = n - 2, n - 1	
solver = FordFulkerson(n,s,t)

solver.addEdge(s, 1, 2);
solver.addEdge(s, 2, 1);
solver.addEdge(s, 0, 7);

solver.addEdge(0, 3, 2);
solver.addEdge(0, 4, 4);

solver.addEdge(1, 4, 5);
solver.addEdge(1, 5, 6);

solver.addEdge(2, 3, 4);
solver.addEdge(2, 7, 8);

solver.addEdge(3, 6, 7);
solver.addEdge(3, 7, 1);

solver.addEdge(4, 5, 8);
solver.addEdge(4, 8, 3);

solver.addEdge(5, 8, 3);

solver.addEdge(6, t, 1);
solver.addEdge(7, t, 3);
solver.addEdge(8, t, 4);


n = 6;
s = n - 1;
t = n - 2;

solver = FordFulkerson(n,s,t)

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
'''

n = 12	
s, t = n - 2, n - 1	
solver = FordFulkerson(n,s,t)

solver.addEdge(s, 0, 10);
solver.addEdge(s, 1, 5);
solver.addEdge(s, 2, 10);

solver.addEdge(0, 3, 10);
solver.addEdge(1, 2, 10);

solver.addEdge(2, 5, 15);
solver.addEdge(3, 1, 2);

solver.addEdge(3, 6, 15);
solver.addEdge(4, 1, 15);

solver.addEdge(4, 3, 3);
solver.addEdge(5, 4, 4);

solver.addEdge(5, 8, 10);
solver.addEdge(6, 7, 10);

solver.addEdge(7, 4, 10);
solver.addEdge(7, 5, 7);
solver.addEdge(6, t, 15);
solver.addEdge(8, t, 10);

print (solver.getMaxFlow())