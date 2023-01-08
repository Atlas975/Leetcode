#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start

from collections import deque


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = deque()

        for r, t in enumerate(temperatures):
            while s and temperatures[s[-1]] < t:
                l = s.pop()
                res[l] = r - l
            s.append(r)
        return res


# @lc code=end
