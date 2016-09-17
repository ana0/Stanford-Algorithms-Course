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
        #print "checking", i
        if i not in explored:
            explored.append(i)
        stack = graph[i]
        while stack:
            next = stack.pop()
            if next not in explored:
                explored.append(next)
                stack.append(next)
                if next in graph:
                    stack = stack + graph[next]
            else:
                if next not in finish_time:
                    finish_time[next] = count
                    count += 1
    return finish_time

def finishing_times(times):
    reversed_times = ["i" for time in times]
    for time in times:
        reversed_times[times[time]] = time
    reversed_times.reverse()
    return reversed_times

def second_pass(graph, times):
    explored = []
    all_paths = []
    for i in times:
        path_size = 1
        print "checking", i
        if i not in explored:
            explored.append(i)
        stack = graph[i]
        while stack:
            next = stack.pop()
            if next not in explored:
                path_size += 1
                explored.append(next)
                if next in graph:
                    stack = stack + graph[next]
        all_paths.append(path_size)
    return all_paths

test = create_reversed_graph("text.txt")
ok = first_pass(test)
# print ok
cats = finishing_times(ok)
ermk = create_graph("text.txt")
print second_pass(ermk, cats)
