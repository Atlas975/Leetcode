#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from collections import deque


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:


        

        # res = deque()

        # for i, curr in enumerate(intervals):
        #     if curr[1] < newInterval[0]:
        #         res.append(curr)
        #     elif curr[0] > newInterval[1]:
        #         res.append(newInterval)
        #         res.extend(intervals[i:])
        #         return res
        #     else:
        #         newInterval = (
        #             min(curr[0], newInterval[0]),
        #             max(curr[1], newInterval[1]),
        #         )

        # res.append(newInterval)
        # return res




# @lc code=end
