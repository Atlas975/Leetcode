#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        occur = Counter(nums)
        try:
            return max(occur[i] + occur[i + 1] for i in occur if i + 1 in occur)
        except ValueError:
            return 0


# @lc code=end
