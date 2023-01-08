#
# @lc app=leetcode id=1779 lang=python3
#
# [1779] Find Nearest Point That Has the Same X or Y Coordinate
#

# @lc code=start
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mind = (-1, float("inf"))

        for i, p in enumerate(points):
            if p[0] == x or p[1] == y:
                man_dist = abs(x - p[0]) + abs(y - p[1])
                if man_dist < mind[1]:
                    mind = (i, man_dist)

        return mind[0]


# @lc code=end
