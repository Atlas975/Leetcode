#
# @lc app=leetcode id=2009 lang=python3
#
# [2009] Minimum Number of Operations to Make Array Continuous
#

# @lc code=start
from bisect import bisect_right
import heapq


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))  # Make `nums` as unique numbers and sort `nums`.

        ans = n
        for i, start in enumerate(nums):
            end = start + n - 1  # We expect elements of continuous array must in range [start..end]
            idx = bisect_right(nums, end)  # Find right insert position
            uniqueLen = idx - i
            ans = min(ans, n - uniqueLen)
        return ans


# @lc code=end
