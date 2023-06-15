#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for i, num in enumerate(nums):
            if (target - num) in dp:
                return (i, dp[target - num])
            dp[num] = i
        return -1


# @lc code=end
