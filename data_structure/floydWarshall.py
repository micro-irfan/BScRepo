class Floyd():
	def __init__(self, n):
		global p_inf
		p_inf = float("inf")
		self.n = n #size of the adjency matrix
		self.dp = [[0 for j in range(self.n)] for i in range(self.n)] #the memo table that will contain APSP soln 2D
		self.next = [[0 for j in range(self.n)] for i in range(self.n)] #matrix used to construct shortest path 2D table
		self.matrix = [[p_inf for j in range(self.n)] for i in range(self.n)]
		for i in range(self.n):
			self.matrix[i][i] = 0


	def addToMatrix(self, u, v, cost):
		self.matrix[u][v] = cost

	def printMatrix(self):
		for i in self.matrix:
			print (*i)

	def printNext(self):
		for i in self.next:
			print (*i)

	def printDP(self):
		for i in self.dp:
			print (*i)


	def floydWarshall(self):
		#m 2d adjency matrix representing the graph	
		self.setup(self.matrix)

		for k in range(self.n):
			for i in range(self.n):
				for j in range(self.n):
					if self.dp[i][k] + self.dp[k][j] < self.dp[i][j]:
						self.dp[i][j] =  self.dp[i][k] + self.dp[k][j]
						self.next[i][j] = self.next[i][k] 

		#Detect and propogate Negative Cycles (optional steps)
		#self.propagateNegativeCycles()
		return self.dp

	def setup(self, m):
		global p_inf
		p_inf = float("inf")
		self.dp = [[0 for j in range(self.n)] for i in range(self.n)] #empty matrix of size n x n
		self.next = [[0 for j in range(self.n)] for i in range(self.n)] #empty integer matrix of size n x n

		for i in range(self.n):
			for j in range(self.n):
				self.dp[i][j] = m[i][j]
				if m[i][j] != p_inf:
					self.next[i][j] = j



	def propagateNegativeCycles(self):
		n_inf = float("-inf")
		for k in range(self.n):
			for i in range(self.n):
				for j in range(self.n):
					if self.dp[i][k] + self.dp[k][j] < self.dp[i][j]:

						self.dp[i][j] = n_inf
						self.next[i][j] = -1

	def reconstructPath(self, s, e):
		#self.printNext()
		path = []
		if self.dp[s][e] == p_inf:
			return "Path Does Not exist"

		at = s
		while at != e:
			if at == -1:
				return "Infinity Loop Due to Negative weight cost"
			path.append(at)
			at = self.next[at][e]

		if self.next[at][e] == -1:
			return None
		path.append(e)
		return path

n = 7
g = Floyd(n)
g.addToMatrix(0,1,2)
g.addToMatrix(0,2,5)
g.addToMatrix(0,6,10)
g.addToMatrix(1,2,2)
g.addToMatrix(1,4,11)
g.addToMatrix(2,6,2)
g.addToMatrix(6,5,11)
g.addToMatrix(4,5,1)
g.addToMatrix(5,4,-2)
#g.printMatrix()
g.floydWarshall()
#print (g.reconstructPath(0,6))

for i in range(n):
	for j in range(n):
		a = g.reconstructPath(i, j)
		print ("Path from {0} to {1} is {2}".format(i, j, a))
		
