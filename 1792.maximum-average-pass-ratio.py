#
# @lc app=leetcode id=1792 lang=python3
#
# [1792] Maximum Average Pass Ratio
#

# @lc code=start
import heapq


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        profit = lambda p, t: (p + 1) / (t + 1) - p / t

        heap = [(-profit(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            _, p, t = heapq.heappop(heap)
            heapq.heappush(heap, (-profit(p + 1, t + 1), p + 1, t + 1))

        return sum(p / t for _, p, t in heap) / len(classes)


# @lc code=end
