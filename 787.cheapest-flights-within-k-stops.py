#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#


# @lc code=start
from collections import deque
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, weight in flights:
            graph[u].append((v, weight))
        distmp = [float("inf")] * n
        distmp[src] = 0
        q = deque([(0, src)])

        for _ in range(k):
            for udist, u in (q.popleft() for _ in range(len(q))):
                for v, weight in graph[u]:
                    if (vdist := udist + weight) < distmp[v]:
                        distmp[v] = vdist
                        q.append((vdist, v))
            q = deque(sorted(q))

        for udist, u in (q.popleft() for _ in range(len(q))):
            for v, weight in graph[u]:
                distmp[v] = min(distmp[v], udist + weight)
        return res if (res := distmp[dst]) != float("inf") else -1

# @lc code=end
