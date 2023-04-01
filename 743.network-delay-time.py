#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start


from collections import defaultdict
import heapq as hq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = [[] for _ in range(n)]
        for u, v, w in times:
            edges[u - 1].append((v - 1, w))
        distmp = [float("inf")] * n
        distmp[k - 1] = 0
        pq = [(0, k - 1)]

        while pq:
            udist, u = hq.heappop(pq)
            if udist > distmp[u]:
                continue
            for v, weight in edges[u]:
                if (vdist := udist + weight) < distmp[v]:
                    distmp[v] = vdist
                    hq.heappush(pq, (vdist, v))
        return res if (res := max(distmp)) < float("inf") else -1


# @lc code=end
