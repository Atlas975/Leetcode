#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
from math import dist


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_origin = lambda p: (dist(p, (0, 0)), p)
        distances = list(map(dist_origin, points))
        heapq.heapify(distances)
        return (heapq.heappop(distances)[1] for _ in range(k))


# @lc code=end
