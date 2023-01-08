#
# @lc app=leetcode id=2365 lang=python3
#
# [2365] Task Scheduler II
#

# @lc code=start
from collections import defaultdict


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        types = defaultdict(int)
        mxtime = 0
        for t in tasks:
            mxtime = max(types[t], mxtime + 1)
            types[t] = mxtime + space + 1
        return mxtime


# @lc code=end
