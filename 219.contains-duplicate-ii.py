#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#


# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idxmp = {}
        for i, num in enumerate(nums):
            if (num in idxmp) and (i - idxmp[num] <= k):
                return True
            idxmp[num] = i
        return False


# @lc code=end
