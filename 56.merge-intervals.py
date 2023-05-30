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
        res = deque([intervals[0]])

        for l, r in intervals[1:]:
            topr = res[-1][1]
            if l <= topr: # overlap occurs, merge
                res[-1][1] = max(r, topr)
            else:
                res.append([l, r])
        return res


# @lc code=end
