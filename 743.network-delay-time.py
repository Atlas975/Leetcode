#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start


import heapq as hq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = [[] for _ in range(n + 1)] # 1-indexed, do not count 0 in result
        for u, v, w in times:
            edges[u].append((v, w))
        distmp = [float("inf")] * (n + 1)
        distmp[k] = 0
        pq = [(0, k)]

        while pq:
            udist, u = hq.heappop(pq)
            if udist > distmp[u]:
                continue
            for v, weight in edges[u]:
                if (vdist := udist + weight) < distmp[v]:
                    distmp[v] = vdist
                    hq.heappush(pq, (vdist, v))
        return res if (res := max(distmp[1:])) < float("inf") else -1


# @lc code=end
