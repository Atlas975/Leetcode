#
# @lc app=leetcode id=1851 lang=python3
#
# [1851] Minimum Interval to Include Each Query
#


# @lc code=start
from collections import deque
import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = deque(sorted(intervals, key=lambda x: x[0]))
        cache = {} # query -> min interval length
        pq = []

        for query in sorted(set(queries)):
            while intervals and intervals[0][0] <= query:
                l, r = intervals.popleft() # pop smallest start
                heapq.heappush(pq, (r - l + 1, r)) # interval length, interval end

            while pq and query > pq[0][1]: # intervals that are too small
                heapq.heappop(pq)
            cache[query] = pq[0][0] if pq else -1

        return (cache[q] for q in queries)

# @lc code=end
