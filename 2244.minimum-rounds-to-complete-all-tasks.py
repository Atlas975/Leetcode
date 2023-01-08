#
# @lc app=leetcode id=2244 lang=python3
#
# [2244] Minimum Rounds to Complete All Tasks
#

# @lc code=start
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        res = 0
        for freq in Counter(tasks).values():
            if freq == 1:
                return -1
            res += (freq + 2) // 3
        return res


# @lc code=end
