from copy import deepcopy

class FenwickTree():
	def __init__(self):
		self.N = 0	#
		self.tree = []  #

	def lsb(self, i):
		return i & -i

	def construct(self, values = []):
		if len(values) == 0:
			print ("Values array cannot be None!")
		else:
			self.N = len(values)
			values.insert(0, 0)
			self.tree = deepcopy(values)
			for i in range (1, len(self.tree)):				
				j = i + self.lsb(i)
				if j <= self.N:
					self.tree[j] += self.tree[i]

		return (self.tree)

	def prefixSum(self, i):
		sum_ = 0 
		while i != 0:
			sum_ += self.tree[i]
			i -= self.lsb(i)
		return sum_

	def rangeQuery(self, i, j):
		if j < i: 
			print ("Make sure j >= i")
		return self.prefixSum(j) - self.prefixSum(i-1)

	def add(self, i, x):
		while i < self.N:
			self.tree[i] += x
			i += self.lsb(i)

	def set(i,k):
		value = self.rangeQuery(i,i)
		self.add(i, k - value)

g = FenwickTree()
#values = [x for x in range(1,17)]
values = [5, -3, 6, 1, 0, -4, 11, 6, 2, 7] #index based 1
#values = [1,4,2,1,3,5,1,2,3]
g.construct(values)
print (g.tree)
#print (g.rangeQuery(3, 7))
lst = []
for a in range(len(values)):
	lst.append(g.prefixSum(a))
print (lst)