#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        edges = []
        for i in range(n):
            edges.extend((i, j) for j in range(i + 1, n) if isConnected[i][j])
        return self.count_components(n, edges)

    def count_components(self, n, edges):
        parent = list(range(n))
        rank = [1] * n

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

        res = n - sum(union(u, v) for u, v in edges)
        return res


# @lc code=end
