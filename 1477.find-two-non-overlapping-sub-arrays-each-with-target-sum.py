#
# @lc app=leetcode id=1477 lang=python3
#
# [1477] Find Two Non-overlapping Sub-arrays Each With Target Sum
#

# @lc code=start
import heapq


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        res = []
        lenheap = []

        def bfs(subarr, path, prev_sum):
            for i, num in enumerate(subarr):
                cur_sum = prev_sum + num
                if cur_sum == target:
                    new_path = path + [num]
                    lenheap.append((len(new_path), new_path))
                elif cur_sum < target:
                    bfs(subarr[i + 1 :], path + [num], cur_sum)

        bfs(arr, [], 0)
        heapq.heapify(lenheap)
        return heapq.heappop(lenheap)[0] + lenheap[0][0] if lenheap else -1


# @lc code=end
