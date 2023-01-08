#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
import heapq


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid


# @lc code=end
