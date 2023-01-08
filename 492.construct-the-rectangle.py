#
# @lc app=leetcode id=492 lang=python3
#
# [492] Construct the Rectangle
#

# @lc code=start
from math import sqrt


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(sqrt(area))
        while (area % w) > 0:
            w -= 1
        return (area // w, w)


# @lc code=end
