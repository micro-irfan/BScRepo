import heapq
from collections import defaultdict

class Dijkstra():
	def __init__(self):
		self.graph = defaultdict(list)

	def addDirectedEdge(self, u, v, cost):
		self.graph[u].append([v, cost])

	def numberofNodes(self, graph):
		lst = []
		for key, value in graph.items():
			if key not in lst:
				lst.append(key)
			for a in value:
				if a[0] not in lst:
					lst.append(a[0])
		return lst

	def getGraph(self):
		print (self.graph) 

	def lazyD(self, source, target):
		number = self.numberofNodes(self.graph)
		INF = ((63**1) - 1)//2
		self.INF = INF
		dist = [INF for x in number]
		prev = [None for x in number]
		vis = [False for x in number]
		dist[0] = 0
	    #pred = {x:x for x in number}
		dist[source] = 0
		PQ = []
		heapq.heappush(PQ, [source, dist[source]])

		while PQ:
			index, minValue = heapq.heappop(PQ)
			vis[index] = True
			if dist[index] < minValue:
				continue
			for edge in self.graph[index]:
				if vis[edge[0]]:
					continue
				newDist = dist[index] + edge[1]
				if newDist < dist[edge[0]]:
					prev[edge[0]] = index
					dist[edge[0]] = newDist
					heapq.heappush(PQ, [edge[0], newDist])

		return dist, prev

	def findShortestPath(self, s, e):
		dist, prev = self.lazyD(s, e)
		path = []
		if (dist[e] == self.INF):
			return path

		at = e
		while at != None:
			path.append(at)
			at = prev[at]

		path = path[::-1]
		return path


adj1 = {0: [(1,-7), (2,-4)], 2:[(3,-2)], 1:[(4,-1)], 3:[(4,-3)]}

g = Dijkstra() 
for key, value in adj1.items():
	for a in value:
		g.addDirectedEdge(key, a[0], a[1])

g.getGraph()
print (g.findShortestPath(0,4))
print (g.lazyD(0,4)[0])
print (g.lazyD(0,4)[1])

