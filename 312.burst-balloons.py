#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + [x for x in nums if x != 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        # ITERATIVE
        for l in reversed(range(n - 1)):
            for r in range(l + 2, n):
                adjprod = nums[l] * nums[r]
                dp[l][r] = max(
                    dp[l][i] + (adjprod * nums[i]) + dp[i][r]
                    for i in range(l + 1, r)
                )
        return dp[0][-1]

        # RECURSIVE
        def dfs(l, r):
            if l > r:
                return 0
            if dp[l][r] != 0:
                return dp[l][r]

            adjprod = nums[l - 1] * nums[r + 1]
            dp[l][r] = max(
                dfs(l, i - 1) + (adjprod * nums[i]) + dfs(i + 1, r)
                for i in range(l, r + 1)
            )
            return dp[l][r]

        return dfs(1, len(nums) - 2)  # exclude 1st and last


# @lc code=end

