# leetcode 128, 1302

class UnionSet():
    def __init__(self):
        pass

    def find(self, edges, nodes):
        roots = nodes
        for edge in edges:
            roots[edge[1]] = edge[0]

        for node in nodes:
            while True:
                root_of_node = roots[node]
                if root_of_node == roots[root_of_node]:
                    break
                else:
                    roots[node] = roots[root_of_node]

        L = {}
        for i, f in enumerate(roots):
            L[f] = []
        for i, f in enumerate(roots):
            L[f].append(i)
            
        print(L)


if __name__ == '__main__':
    union_set = UnionSet()
    edges = [[0, 1], [0, 4], [1, 2], [1, 3], [5, 6], [6, 7], [7, 5], [8, 9]]
    nodes = list(range(10))
    union_set.find(edges, nodes)
