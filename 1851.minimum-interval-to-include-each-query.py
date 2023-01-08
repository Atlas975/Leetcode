#
# @lc app=leetcode id=1851 lang=python3
#
# [1851] Minimum Interval to Include Each Query
#

# @lc code=start
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        lens = [interval[1] - interval[0] + 1 for interval in intervals]
        res = []
        for query in queries:
            low = float("inf")
            for i, interval in enumerate(intervals):
                if interval[0] <= query <= interval[1]:
                    low = min(low, lens[i])
            if low == float("inf"):
                res.append(-1)
            else:
                res.append(low)
        return res


# @lc code=end
