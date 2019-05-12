import numpy as np
from BasicGraph import Graph

# topological sorting for Directed Acyclic Graph
def topological_sort(graph):
    vertices_list = list(graph.get_vertices())
    in_degrees = dict((u, 0) for u in vertices_list)

    # count in degrees
    for u in vertices_list:
        out_vertex = graph.get_vertex(u).get_neighbors()
        for v in out_vertex:
            in_degrees[v.value] += 1

    Q = [u for u in vertices_list if in_degrees[u] == 0]

    # the final order list
    S = []
    while Q:
        u = Q.pop()
        S.append(u)

        for v in graph.get_vertex(u).get_neighbors():
            # remove the outs of current vertex
            in_degrees[v.value] -= 1

            if in_degrees[v.value] == 0:
                Q.append(v.value)

    print(S)

# path length to a vertex in a graph with single origin and unweighted edge
def unweighted(v):
    queue=[]
    path_length={}
    path_length[v]=0
    queue.append(v)

    # something like dynamic programming
    while queue:
        v=queue.pop(0)
        for i in v.get_neighbors():
            if i not in path_length:
                path_length[i]=path_length[v]+1
                queue.append(i)

    print(path_length)

def Dijkstra():
    pass

def Prim():
    pass

def Kruskal():
    pass

if __name__ == '__main__':
    graph = Graph()
    element_list = ['a', 'b', 'c', 'd', 'e', 'f']
    edge_list = [('a','b',3),('a','f',5),('b','c',4),('b','d',10),('b','f',9),('c','d',3),('d','e',5),('d','f',7),('e','f',4)]
    for element in element_list:
        graph.add_vertex(element)
    for edge in edge_list:
        graph.add_edge(edge[0], edge[1], edge[2])

    for element in graph:
        print(element.adj)

    # top sort
    topological_sort(graph)

    # unweighted path length
    unweighted(graph.vertexlist['a'])