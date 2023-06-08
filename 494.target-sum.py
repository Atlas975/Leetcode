#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
from collections import defaultdict
from functools import cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for num in nums:
            tdp = defaultdict(int)
            for s, cnt in dp.items():
                tdp[s + num] += cnt
                tdp[s - num] += cnt
            dp = tdp
        return dp.get(target, 0)
        # tsum = sum(nums)
        # if abs(target) > tsum or (tsum - target) % 2:
        #     return 0
        # halfdif = (tsum - target) // 2
        # dp = [1] + ([0] * halfdif)

        # for num in nums:
        #     for j in reversed(range(num, halfdif + 1)):
        #         dp[j] += dp[j - num]
        # return dp[-1]

        # @cache
        # def dfs(i, dp):
        #     if i == len(nums):
        #         return dp.get(target, 0)
        #     tdp = defaultdict(int)
        #     for s in dp:
        #         tdp[s + nums[i]] += dp[s]
        #         tdp[s - nums[i]] += dp[s]
        #     return dfs(i + 1, tdp)
        # return dfs(0, {0: 1})


# @lc code=end
