#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#


# @lc code=start
import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        need = set(range(len(points)))
        pq = [(0, 0)]  # (dist, node)
        res = 0

        while need:
            while pq[0][1] not in need:
                heapq.heappop(pq)
            udist, u = heapq.heappop(pq)
            need.remove(u)
            res += udist
            x1, y1 = points[u]
            for v, (x2, y2) in ((i2, points[i2]) for i2 in need):
                heapq.heappush(pq, (abs(x1 - x2) + abs(y1 - y2), v))
        return res
    

        n = len(points)
        graph = [[] for _ in range(n)]
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i + 1 :], i + 1):
                dist = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append((dist, j))
                graph[j].append((dist, i))

        res = 0
        visited = set()
        pq = [(0, 0)]  # (dist, node)
        while len(visited) < n:
            udist, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            res += udist
            for vdist, v in graph[u]:
                if v not in visited:
                    heapq.heappush(pq, (vdist, v))
        return res


# @lc code=end
