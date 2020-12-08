import re
import networkx as nx
import string

with open('input.txt', 'r') as f:
    data = list(f.read().split("\n"))

graph = nx.DiGraph()

# Create graph
for b in data:
    color = re.search('^[a-z ]+(?=bags)', b).group().strip()

    subcolors = re.finditer(r'[0-9][a-z ]+((?=,)|(?=.))+', b)

    for subcolor in subcolors:
        weight = int(subcolor.group().strip(string.ascii_letters + ' '))
        subcolor = ''.join([i for i in subcolor.group() if not i.isdigit()]).replace('bags', '').replace('bag',
                                                                                                         '').strip()
        graph.add_edge(color, subcolor)
        graph[color][subcolor]['weight'] = weight


def get_successors(node, c):
    if len(list(graph.successors(node))) == 0:
        return c

    sum = c

    for n in graph.successors(node):
        w = graph[node][n]['weight']
        sum += get_successors(n, w * c)

    return sum


print(get_successors('shiny gold', 1))  # 158494
