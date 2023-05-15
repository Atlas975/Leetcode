#
# @lc app=leetcode id=1465 lang=python3
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#


# @lc code=start
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        max_gap = lambda size, cuts: max(
            cuts[0],
            size - cuts[-1],
            max((cuts[i] - cuts[i - 1] for i in range(1, len(cuts))), default=0),
        )
        horizontalCuts.sort()
        verticalCuts.sort()
        return max_gap(h, horizontalCuts) * max_gap(w, verticalCuts) % (10**9 + 7)


# @lc code=end
