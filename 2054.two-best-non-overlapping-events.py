#
# @lc app=leetcode id=2054 lang=python3
#
# [2054] Two Best Non-Overlapping Events
#

# @lc code=start
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        is_overlap = lambda a, b: max(a[0], b[0]) <= min(a[1], b[1])
        n = len(events)
        res = 0
        for i in range(n):
            a = events[i]
            b = events[i + 1] if i + 1 < n else None
            for j in range(i + 1, n):
                if not is_overlap(events[i], events[j]):
                    res = max(res, events[i][2] + events[j][2])
        return res


# @lc code=end
