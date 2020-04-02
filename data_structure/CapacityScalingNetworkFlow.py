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

class CapacityScaling(NetworkFlowSolverBase, Edge):
	def __init__(self,n,s,t):
		super().__init__(n,s,t)
		self.delta = 0

	def addEdge(self, from_, to, capacity):
		super().addEdge(from_, to, capacity)
		self.delta = max(self.delta, capacity)
		#print (self.delta)

	def highestOneBit(self, n):
		if (n == 0): 
			return 0 
  
		msb = 0; 
		while (n > 0): 
			n = int(n / 2) 
			msb += 1

		msb -= 1
		return (1 << msb)

	def solve(self):
		p_inf = float("inf")
		self.delta = self.highestOneBit(self.delta)
		#print (self.delta)

		while self.delta>0:
			self.markNodeAsUnvisited()
			f = self.dfs(self.s, p_inf)
			if f == None or f == 0:
				break
			self.maxflow += f
			self.delta /= 2
			#print (self.delta)

	def dfs(self, node, flow):
		if node == self.t:
			return flow
		self.visit(node)

		edges = self.graph[node]
		for edge in edges:
			cap = edge.remainingCapacity()
			if cap >= self.delta and not self.visited_(edge.to):
				bottleNeck = self.dfs(edge.to, min(flow, cap))
				#if bottleNeck:
				if bottleNeck > 0:
					edge.augment(bottleNeck)
					return bottleNeck
		return 0

n = 6;
s = n - 1;
t = n - 2;


solver = CapacityScaling(n,s,t)

    #Source edges
solver.addEdge(s, 0, 6)
solver.addEdge(s, 1, 14)

   # Sink edges
solver.addEdge(2, t, 11)
solver.addEdge(3, t, 12)

   # Middle edges
solver.addEdge(0, 1, 1)
solver.addEdge(0, 2, 5)
solver.addEdge(1, 2, 7)
solver.addEdge(1, 3, 10)
solver.addEdge(2, 3, 1)

#20
'''

n = 6;
s = n - 1;
t = n - 2;

solver = CapacityScaling(n,s,t)

    # Source edges
solver.addEdge(s, 0, 10);
solver.addEdge(s, 1, 10);

    # Sink edges
solver.addEdge(2, t, 10);
solver.addEdge(3, t, 10);

    # Middle edges
solver.addEdge(0, 1, 2);
solver.addEdge(0, 2, 4);
solver.addEdge(0, 3, 8);
solver.addEdge(1, 3, 9);
solver.addEdge(3, 2, 6);

'''
print (solver.getMaxFlow())#19

