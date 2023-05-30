#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res, end = 0, intervals[0][0]

        for l, r in intervals[1:]:
            if l >= end: # no overlap, keep this interval
                end = r
            else: # overlap, 1 more interval to remove
                res += 1
        return res



# @lc code=end
