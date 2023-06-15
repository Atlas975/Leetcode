#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        res = 1
        for i, (x1, y1) in enumerate(points[:-1]): # O(n^2)
            slopes = {}  # slope: count
            for x2, y2 in points[i + 1 :]:
                s = (y2 - y1) / (x2 - x1) if x2 != x1 else "inf"
                slopes[s] = slopes.get(s, 1) + 1
            res = max(res, max(slopes.values(), default=0))
        return res


# @lc code=end
