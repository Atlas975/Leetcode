#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from collections import deque


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])
        res_stack = deque([intervals[0]])

        for l, r in intervals[1:]:
            topr = res_stack[-1][1]
            if l <= topr:
                res_stack[-1][1] = max(r, topr)
            else:
                res_stack.append([l, r])

        return res_stack


# @lc code=end
