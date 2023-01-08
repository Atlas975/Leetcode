#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
# import library to flatten list


from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {i: i for i in range(1, n + 1)}
        rank = defaultdict(int)

        def find(u):
            while (u := parent[u]) != parent[u]:
                parent[u] = parent[parent[u]]
            return u

        def union(u, v):
            root_u, root_v = find(u), find(v)
            if root_u == root_v:
                return True

            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
            return False

        return next((n1, n2) for n1, n2 in edges if union(n1, n2))
