from functools import reduce
from typing import List


class UnionFind:
    def count_components(self, edges: List[List[int]]) -> int:

        nodes = set(reduce(lambda x, y: x + y, edges))
        n = len(nodes)
        parent = {i: i for i in nodes}
        rank = {i: 1 for i in nodes}

        def find(u):
            while u != parent[u]:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        def union(u, v):
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return 0

            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res


if __name__ == "__main__":
    print(UnionFind().count_components([[0, 1], [1, 2], [3, 4], [5, 8]]))
    print(UnionFind().count_components([[0, 1], [1, 2], [2, 3], [3, 4]]))
