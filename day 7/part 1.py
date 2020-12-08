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


def get_predecessors(node, c):
    if len(list(graph.predecessors(node))) == 0:
        return c

    for n in graph.predecessors(node):
        c.add(n)
        get_predecessors(n, c)

    return c


# Count all predecessors
print(len(get_predecessors('shiny gold', set())))  # 235
