import random

test_dict = {"A": ["C"],
            "B": ["A"],
            "C": ["B", "D"],
            "D": ["F", "H"],
            "E": ["D"],
            "F": ["E"],
            "G": ["I"],
            "H": ["G"],
            "I": ["H"]}

def create_graph(filename):
    f = open(filename, 'r')
    graph = {}
    for line in f: 
        line = line.split()
        if line[0] in graph:
            graph[line[0]].extend(line[1:])
        else:
            graph[line[0]] = line[1:]
    return graph

def create_reversed_graph(filename):
    f = open(filename, 'r')
    graph = {}
    for line in f: 
        line = line.split()
        if line[1] in graph:
            graph[line[1]].extend(line[:1])
        else:
            graph[line[1]] = line[:1]
    return graph

def first_pass(graph):
    explored = []
    count = 0
    finish_time = {}
    for i in graph:
        print "checking", i
        if i not in explored:
            explored.append(i)
        stack = graph[i]
        while stack:
            next = stack.pop()
            if next not in explored:
                explored.append(next)
                stack.append(next)
                stack = stack + graph[next]
            else:
                if next not in finish_time:
                    finish_time[next] = count
                    count += 1
    return finish_time

test = create_reversed_graph("text.txt")
print test
