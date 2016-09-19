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
            graph[int(line[0])].extend([int(i) for i in line[1:]])
        else:
            graph[int(line[0])] = [int(i) for i in line[1:]]
    return graph

def create_reversed_graph(filename):
    f = open(filename, 'r')
    graph = {}
    for line in f: 
        line = line.split()
        if line[1] in graph:
            graph[int(line[1])].extend([int(i) for i in line[:1]])
        else:
            graph[int(line[1])] = [int(i) for i in line[:1]]
    return graph

def first_pass(graph):
    explored = set()
    count = 0
    finish_time = {}
    for i in graph:
        print "checking", i
        explored.add(i)
        stack = graph[i]
        while stack: 
            print "stack is", stack
            next = stack.pop()
            if next not in explored:
                explored.add(next)
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
    explored = set()
    all_paths = []
    for i in times:
        path_size = 1
        print "checking", i
        explored.add(i)
        stack = graph[i]
        while stack:
            next = stack.pop()
            if next not in explored:
                path_size += 1
                explored.add(next)
                if next in graph:
                    stack = stack + graph[next]
        all_paths.append(path_size)
    return all_paths

def get_max_five(all_paths):
    for i in range(6):
        tuft = max(all_paths)
        all_paths.remove(tuft)
        print tuft

test = create_reversed_graph("SCC.txt")
print "created reversed graph"
print
ok = first_pass(test)
print "computed finishing times"
print 
cats = finishing_times(ok)
print "formatted finishing_times"
print
ermk = create_graph("SCC.txt")
print "create non-reversed graph"
print
hulo = second_pass(ermk, cats)
print "computed strongly connected components"
print
whoo = get_max_five(hulo)
