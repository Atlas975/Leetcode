#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        slope_calc = lambda p1, p2: (
            (p1[1] - p2[1]) / (p1[0] - p2[0]) if (p1[0] - p2[0]) != 0 else float("inf")
        )

        res = 1
        slopes = defaultdict(lambda: 1)
        for i, p1 in enumerate(points):
            slopes.clear()
            for p2 in points[i + 1 :]:
                slope = slope_calc(p1, p2)
                slopes[slope] += 1
                res = max(res, slopes[slope])
        return res


# @lc code=end
