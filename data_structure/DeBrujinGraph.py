from eulerian_path import EulerPath
from collections import defaultdict
'''
Patterns = ['CTTA',
     'ACCA',
     'TACC',
     'GGCT',
     'GCTT',
     'TTAC']
'''
k = 15
Patterns = []
with open('trial.txt', 'r') as f:
	for line in f:
		line = line.strip('\n')
		Patterns.append(line)

print (len(Patterns))
def DeBrujinString(Patterns ,k):
	nodes = defaultdict(list)
	length = len(Patterns[0])
	k = k-1
	for a in Patterns:
		a1 = a[:k]
		a2 = a[1:]
		nodes[a1].append(a2)
	return nodes

a = (DeBrujinString(Patterns, k))


g = EulerPath()

for key, value in a.items():
	for a in value:
		g.addEdges(key, a)

#g.getGraph()
a = g.findEulerianPath()

def StringSpelled(lst):
	string = lst[0]
	for i in lst[1:]: 
		string += i[-1]

	return (string)

print (StringSpelled(a[1])) 
print (a[2:])

