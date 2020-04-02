from collections import defaultdict
from singly_linked_list import linked_list

class EulerPath():
	def __init__(self):
		self.graph = defaultdict(list)
		self.edges = 0
		self.vertices = 0
		self.inlst = [0]
		self.outlst = [0] 
		self.path = linked_list()
		self.StrDictToIndex = {}

	def addEdges(self, u, v):
		self.graph[u].append(v)
		self.edges += 1
		self.numberOfVertices()

		##Check if String
		#if isinstance(u,str) and isinstance(v,str):
		lst = []
		for key, value in self.graph.items():
			if key not in lst:
				lst.append(key)
				for a in value:
					if a not in lst:
						lst.append(a)

		for a in lst:
			if a not in self.graph.keys():
				self.graph[a].append(None)

		#print (len(lst))
		'''			
		else:
			highestKey = max(self.graph)
			for i in range(highestKey):
				if not self.graph[i]:
					self.graph[i].append(None)
		'''
		for key, value in self.graph.items():
			if None in value and len(value) > 1:
				value.remove(None)

	def numberOfVertices(self):
		self.vertices = len(self.graph)
		self.inlst = [0] * self.vertices
		self.outlst = [0] * self.vertices

	def getGraph(self):
		print (self.graph)

	def findEulerianPath(self):
		lst = []
		for key, value in self.graph.items():
			if key not in lst:
				lst.append(key)

		count = 0
		for key in self.graph.keys():
			self.StrDictToIndex[key] = count
			count += 1
				
		print (1, len(self.StrDictToIndex))	
		print (1, len(self.graph))	
		#print (self.StrDictToIndex)

		self.CountInOutDegree()

		if not self.graphHasEulerianPath():
			print (False)

		self.dfs(self.findStartNode())

		finaOutput = []
		a = self.path.display()
		for i in a:
			for key, value in self.StrDictToIndex.items():
				if i == value:
					finaOutput.append(key)

		if self.path.length() == self.edges+1:
			return finaOutput
		return False, finaOutput, self.edges, self.path.length()

	def CountInOutDegree(self):
		for edges in self.graph:
			edges2 = self.graph.get(edges)
			if edges2 != [None]:
				for edge in edges2:
					edges = self.StrDictToIndex.get(edges)
					self.outlst[edges] += 1 
					if edge != None:
						#print(edge)
						edge = self.StrDictToIndex.get(edge)
						if edge != None: ###debug needed
						#print (edge)
							self.inlst[edge] += 1

	def graphHasEulerianPath(self):
		start_node, end_node = 0, 0

		for i in range(self.vertices):
			if (self.outlst[i] - self.inlst[i]) > 1 or (self.inlst[i] - self.outlst[i]) >1:
				return False
			elif self.outlst[i] - self.inlst[i] == 1:
				start_node += 1
			elif self.inlst[i] - self.outlst[i] == 1:
				end_node +=1

		return (end_node == 0 and start_node == 0) or (end_node == 1 and start_node == 1)

	def findStartNode(self):
		start = 0
		for i in range(self.vertices):
			if self.outlst[i] - self.inlst[i] == 1:
				return i

			if self.outlst[i] > 0:
				start = i 

		return start

	def dfs(self, at):
		while self.outlst[at] != 0:
			self.outlst[at] -= 1
			#get key from Value
			for key, value in self.StrDictToIndex.items():
				if value == at:
					at1 = key 
			next_edge = self.graph.get(at1)
			next_edges = []
			for i in next_edge:
				next_edges.append(self.StrDictToIndex.get(i))
			next_edge = next_edges[self.outlst[at]]
			if next_edge != None:
				self.dfs(next_edge)

		self.path.insert(0, at)


