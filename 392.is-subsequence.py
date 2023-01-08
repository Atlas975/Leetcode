#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sn, tn = len(s), len(t)
        i, j = 0, 0
        while i < sn and j < tn:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == sn


# @lc code=end
