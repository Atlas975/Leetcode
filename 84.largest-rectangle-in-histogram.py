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
            while s and h < s[-1][1]: # previous rec cant extend to current
                l, h0 = s.pop()
                mxrea = max(mxrea, h0 * (r - l))
            s.append((l, h)) # l is lestmost >= h

        return max(mxrea, max(h * (len(heights) - l) for l, h in s))


# @lc code=end
