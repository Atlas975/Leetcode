#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res, end = 0, float("-inf")
        for l, r in sorted(intervals, key=lambda x: x[1]):
            if l >= end:
                end = r
            else:
                res += 1
        return res

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        i1 = intervals[0]
        is_overlap = lambda a, b: max(a[0], b[0]) <= min(a[1], b[1])

        for i in range(1, len(intervals)):
            if is_overlap(i1, intervals[i]):
                return False
            i1 = max(i1, intervals[i], key=lambda x: x[1])


# @lc code=end
