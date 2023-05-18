#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dp = [0] * len(nums)

        for i in range(k):
            dp[i] = nums[i]

        for i in range(k, len(nums)):
            dp[i] = max(dp[i - 1], nums[i])

        return dp

# @lc code=end
