#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start


from functools import cache


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + [x for x in nums if x != 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for r in range(2, n - 1):  
            for l in range(r - 2, -1, -1): 
                adjprod = nums[l] * nums[r]
                dp[l][r] = max(
                    dp[l][i] + (adjprod * nums[i]) + dp[i][r]
                    for i in range(l + 1, r)  # exclude first & last
                )
        return dp[0][n - 1]

        # RECURSIVE
        def dfs(l, r):
            if l > r:
                return 0
            if dp[l][r] != 0:
                return dp[l][r]

            adj = nums[l - 1] * nums[r + 1]
            dp[l][r] = max(
                dfs(l, i - 1) + (adj * nums[i]) + dfs(i + 1, r)
                for i in range(l, r + 1)
            )
            return dp[l][r]
        return dfs(1, len(nums) - 2)  # exclude first and last


# @lc code=end

Solution().maxCoins([3, 1, 5, 8])
