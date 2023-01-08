#
# @lc app=leetcode id=1218 lang=python3
#
# [1218] Longest Arithmetic Subsequence of Given Difference
#

# @lc code=start
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for num in arr:
            dp[num] = dp[num - difference] + 1
        return max(dp.values())


# @lc code=end
