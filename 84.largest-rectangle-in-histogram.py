#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
from collections import deque


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mxrea, s = 0, deque()
        for r, h in enumerate(heights):
            l = r
            while s and s[-1][1] > h:
                l, h0 = s.pop()
                mxrea = max(mxrea, h0 * (r - l))
            s.append((l, h))

        n = len(heights)
        return max(mxrea, max((h * (n - l) for l, h in s)))


# @lc code=end
