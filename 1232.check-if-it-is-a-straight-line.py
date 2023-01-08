#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        (x0, y0), (x1, y1) = coordinates[:2]
        basex, basey = x1 - x0, y1 - y0

        return all(basex * (y - y0) == (x - x0) * basey for x, y in coordinates[2:])


# @lc code=end
