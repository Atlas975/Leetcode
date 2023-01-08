#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from os.path import commonprefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return commonprefix(strs)
        # pref = strs[0]
        # for word in strs[1:]:
        #     j = 0
        #     n = min(len(pref), len(word))
        #     while j < n and pref[j] == word[j]:
        #         j += 1
        #     pref = pref[:j]
        # return pref


# @lc code=end
