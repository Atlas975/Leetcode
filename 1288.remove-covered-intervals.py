#
# @lc app=leetcode id=1288 lang=python3
#
# [1288] Remove Covered Intervals
#

# @lc code=start
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[0])
        res, prev = 1, intervals[0]

        for l, r in intervals[1:]:
            if prev[1] < r:
                if prev[0] != l:
                    res += 1
                prev = (l, r)

        return res


# @lc code=end
