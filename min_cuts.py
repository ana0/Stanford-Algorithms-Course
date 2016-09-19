import random
import math
import copy

def create_graph(filename):
    f = open(filename, 'r')
    graph = {}
    # text = f.readline()
    # print text.split()
    for line in f: 
        line = line.split()
        graph[line[0]] =line[1:]
    return graph

test_graph = create_graph('MinCutsGraph.txt')

debug_graph = {'1':['B','G','H'],
            'B':['1','G','H','C'],
            'C':['B','F','D','E'],
            'D':['C','F','E'],
            'E':['C','F','D'],
            'F':['G','C','D','E'],
            'G':['F','B','1','H'],
            'H':['B','G','1']}

def repeat(func): 
    def find_limit(args):
        num_repetitions = int((len(args)^2)*math.log(len(args)))
        values = []
        for i in range(num_repetitions):
            g = copy.deepcopy(args)
            values.append(func(g))
        return min(values)
    return find_limit

@repeat
def min_cuts_outer(L): 
    return min_cuts(L)

def min_cuts(graph):
    if len(graph) == 2:
        return len(graph.items()[0][1])
    vert = random.choice(graph.keys())
    edge = random.choice(graph[vert]) 
    graph[vert+'+'+edge] = [i for i in graph[vert] + graph[edge] if i != vert 
        and i != edge]
    del graph[vert]
    del graph[edge]
    to_check = set(graph[vert+'+'+edge]) 
    for item in to_check:
        graph[item] = [i if i != vert and i != edge else vert+'+'+edge for i in 
            graph[item]]
    return min_cuts(graph)

def min_cuts_iter(graph):
    num_repetitions = int((len(graph)^2)*math.log(len(graph)))
    values = []
    for i in range(num_repetitions):
        g = copy.deepcopy(graph)
        values.append(min_cuts(g))
    return min(values)

print min_cuts_iter(test_graph)
# print min_cuts_outer(test_graph)


