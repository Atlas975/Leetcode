#
# @lc app=leetcode id=1986 lang=python3
#
# [1986] Minimum Number of Work Sessions to Finish the Tasks
#

# @lc code=start
import heapq as hq


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        # tasks = [-t for t in tasks]
        hq.heapify(tasks)
        res = 0
        while tasks:
            res += 1
            time = sessionTime
            while tasks and tasks[0] <= time:
                time -= hq.heappop(tasks)
                # print(time, tasks)
                # time-=hq.heappop(tasks)
                # print(time)
        return res


# @lc code=end
