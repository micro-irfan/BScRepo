
class indexedPQ():
	def __init__(self):
		self.keys = {}
		self.values = []
		self.pm = [] #position Mapping
		self.im = []
		self.sz = 0 ##current Size 

	def construct(self,ki,value):
		self.keys[ki] = value

	def setup(self):
		self.sz = 

	def insert(self, ki, value):
		self.values[ki] = value
		self.pm[ki] = self.sz
		self.im[self.sz] = ki

		self.swim(self.sz)
		self.sz += 1

	def swim(self, i):
		p = (i-1)/2
		while i > 0 and self.less(i, p):
			self.swap(i, p)
			i = p 
			p = (i-1)/2

	def swap(self, i, j):
		self.pm[self.im[j]] = i
		self.pm[self.im[i]] = j
		tmp = self.im[i]
		self.im[i] = self.im[j]
		self.im[j] = tmp

	def less(self, i, j):
		return self.values[self.im[i]] < self.values[self.im[j]]

	def remove(self, ki):
		i = self.pm[ki]
		self.swap(i, self.sz)
		self.sz -= 1
		self.sink(i)
		self.swim(i)
		self.values[ki] = None
		self.pm[ki] = -1
		self.im[self.sz] = -1

	def sink(self, i):
		while True:
			left = 2*i + 1
			right = 2*i + 2
			smallest = left

			if right < self.sz and self.less(right, left):
				smallest = right

			if left >= self.sz or self.less(i, smallest):
				break

			self.swap(smallest, i)
			i = smallest 

	def decreaseKey(self, ki, value):
		if self.less(value, self.values[ki]):
			self.values[ki] = value
			self.swim(self.pm[ki])

	def increaseKey(self, ki, value):
		if self.less(self.values[ki], value):
			self.values[ki] = value
			self.sink(self.pm[ki])
