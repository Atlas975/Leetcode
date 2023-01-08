#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        j = 0
        seen = {}
        for i, c in enumerate(s):
            if c in seen:
                j = max(j, seen[c] + 1)
            seen[c] = i
            res = max(res, i - j + 1)
        return res


# @lc code=end
