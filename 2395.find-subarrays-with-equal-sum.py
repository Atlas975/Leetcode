#
# @lc app=leetcode id=2395 lang=python3
#
# [2395] Find Subarrays With Equal Sum
#

# @lc code=start
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        sums = set()
        for i in range(n - 1):
            total = sum(nums[i : i + 2])
            if total in sums:
                return True
            sums.add(total)
        return False


# @lc code=end
