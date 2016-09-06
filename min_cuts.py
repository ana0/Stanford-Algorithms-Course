import random

test_graph = {'A':['B','G','H'],
			'B':['A','G','H','C'],
			'C':['B','F','D','E'],
			'D':['C','F','E'],
			'E':['C','F','D'],
			'F':['G','C','D','E'],
			'G':['F','B','A','H'],
			'H':['B','G','A']}

def min_cuts(graph):
	if len(graph) == 2:
		return len(graph.items()[0][1])
	vert = random.choice(graph.keys())
	edge = random.choice(graph[vert]) 
	graph[vert+edge] = [i for i in graph[vert] + graph[edge] if i != vert 
		and i != edge]
	del graph[vert]
	del graph[edge]
	to_check = set(graph[vert+edge]) 
	for item in to_check:
		graph[item] = [i if i != vert and i != edge else vert+edge for i in 
			graph[item]]
	return min_cuts(graph)


print min_cuts(test_graph)