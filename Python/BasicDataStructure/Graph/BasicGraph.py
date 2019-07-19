import numpy as np

class Vertex(object):
    def __init__(self, value):
        self.value = value
        self.adj = dict()

    def add_neighbor(self, nbr, weight=0):
        self.adj[nbr] = weight

    def get_neighbors(self):
        return self.adj.keys()

class Graph(object):
    def __init__(self):
        self.vertexlist = dict()
        self.size = 0

    def add_vertex(self, key):
        vertex = Vertex(key)
        self.vertexlist[key] = vertex
        self.size += 1

    def get_vertex(self, key):
        return self.vertexlist.get(key)

    def add_edge(self, f, t, weight=0):
        if f not in self.vertexlist:
            self.add_vertex(f)
        if t not in self.vertexlist:
            self.add_vertex(t)
        self.vertexlist[f].add_neighbor(self.vertexlist[t], weight)

    def get_vertices(self):
        return self.vertexlist.keys()

    def __iter__(self):
        return iter(self.vertexlist.values())

    def __contains__(self, key):
        if key in self.vertexlist:
            return True
        else:
            return False


if __name__ == '__main__':
    graph = Graph()
    element_list = ['a', 'b', 'c', 'd', 'e', 'f']
    edge_list = [('a', 'b', 3), ('a', 'f', 5), ('b', 'c', 4), ('b', 'd', 10), ('b', 'f', 9), ('c', 'd', 3),
                 ('d', 'e', 5), ('d', 'f', 7), ('e', 'f', 4)]
    for element in element_list:
        graph.add_vertex(element)
    for edge in edge_list:
        graph.add_edge(edge[0], edge[1], edge[2])

    print(list(graph.get_vertices()))