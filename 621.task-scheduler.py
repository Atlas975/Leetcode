#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from collections import Counter, deque
import heapq as hq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q, time = deque(), 0
        mxheap = [-cnt for cnt in Counter(tasks).values()]
        hq.heapify(mxheap)

        while mxheap:
            time += 1
            if tasks := hq.heappop(mxheap) + 1:
                q.append((tasks, time + n))
            if not q:
                continue
            if not mxheap:
                tasks, time = q.popleft()
                hq.heappush(mxheap, tasks)
            elif time == q[0][1]:
                hq.heappush(mxheap, q.popleft()[0])
        return time


# @lc code=end
