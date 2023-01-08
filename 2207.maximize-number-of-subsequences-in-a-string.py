#
# @lc app=leetcode id=2207 lang=python3
#
# [2207] Maximize Number of Subsequences in a String
#

# @lc code=start


class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        total, cnt0, cnt1 = 0, 0, 0
        for c in text:
            if c == pattern[1]:
                total += cnt0
                cnt1 += 1
            if c == pattern[0]:
                cnt0 += 1
        return total + max(cnt0, cnt1)


# @lc code=end
