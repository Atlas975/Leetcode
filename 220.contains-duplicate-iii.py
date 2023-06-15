#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
from sortedcontainers import SortedList

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        bukts = {}
        valueDiff += 1

        for i, num in enumerate(nums):
            b = num // valueDiff
            if b in bukts:
                return True
            if b - 1 in bukts and abs(bukts[b - 1] - num) < valueDiff:
                return True
            if b + 1 in bukts and abs(bukts[b + 1] - num) < valueDiff:
                return True
            bukts[b] = num
            if i >= indexDiff:
                del bukts[nums[i - indexDiff] // valueDiff]
# @lc code=end

