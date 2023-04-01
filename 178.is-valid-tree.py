from itertools import starmap
from typing import List


class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))
        rank = [1] * n

        def find(u):
            while (u := parent[u]) != parent[u]:
                parent[u] = parent[parent[u]]
            return u

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru == rv:
                return False

            if rank[ru] > rank[rv]:
                parent[rv] = ru
            elif rank[ru] < rank[rv]:
                parent[ru] = rv
            else:
                parent[rv] = ru
                rank[ru] += 1
            return True

        return len(edges) == n - 1 and all(starmap(union, edges))
        # write your code here


print(
    "No of connected components: ",
    Solution().valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]),
)
