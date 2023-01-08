#
# @lc app=leetcode id=1828 lang=python3
#
# [1828] Queries on Number of Points Inside a Circle
#

# @lc code=start
from math import dist


class Solution:
    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        return [sum(dist(p, (c[0], c[1])) <= c[2] for p in points) for c in queries]


# @lc code=end
