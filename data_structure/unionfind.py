class UnionFind():
	def __init__(self):
		#Number of elements in the union find
		self.size = 0 
		#Used to track the sizes of each component
		self.sz = []
		#id[i] points to the parent of i, if id[i] = i then i is a root node
		self.id = []
		#Tracks the number of components in the union find
		self.numComponents = 0

	def WeightedQuickUnionUF(self, n):
		self.size = n
		if self.size <= 0:
			print ("Size <= 0 is not allowed")

		self.components = n
		self.sz = [0] * n
		self.id = [0] * n

		for i in range(self.size):
			self.id[i] = i
			self.sz[i] = 1

	# Find which component/set 'p' belongs to, takes amortized constant time.
	def find(self, p):
		## Find the root of the component/set
		root = p 
		while root != self.id[root]:
			root = self.id[root]

		#Compress the path leading back to the root.
     	#Doing this operation is called "path compression"
     	#and is what gives us amortized time complexity.
		while p != root:
			nextV = self.id[p]
			self.id[p] = root
			p = nextV

		return root	

	#within the same set/components
	def connected(self, p, q):
		return self.find(p) == self.find(q)

	def componentSize(size, p):
		return self.sz[self.find(p)]

	def size1(self, p):
		return self.sz[self.find(p)]

	def components(self):
		return self.numComponents

	def unify(self, p, q):
		root1 = self.find(p)
		root2 = self.find(q)

		if root1 == root2:
			return

		if self.sz[root1] < self.sz[root2]:
			self.sz[root2] += self.sz[root1]
			self.id[root1] = root2
		else:
			self.sz[root1] += self.sz[root2]
			self.id[root2] = root1

		self.numComponents -= 1

	def printId(self):
		print ('Root Node: ' ,self.id)
		print ('Size: ' , self.sz)
		#totalSize = 0
		#for a in self.sz:
			#totalSize += a
		#print ('Total Size: ' , totalSize)
'''
g = UnionFind()

g.WeightedQuickUnionUF(10)
g.unify(4,3)
g.unify(3,8)
g.unify(6,5)
g.unify(9,4)
g.unify(2,1)
g.unify(8,9)
g.unify(5,0)
g.unify(7,2)
g.unify(6,1)
g.unify(1,0)
g.unify(6,7)
g.printId()

g.WeightedQuickUnionUF(8)
g.unify(0,1)
g.unify(2,3)
g.unify(4,5)
g.unify(6,7)
g.unify(0,2)
g.unify(4,6)
g.unify(0,4)
g.printId()
'''
