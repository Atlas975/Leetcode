#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = [float("inf")] * 128
        res, l = 0, 0
        for i, c in enumerate(s):
            idx = ord(c)
            if seen[idx] != float("inf"):
                l = max(l, seen[idx] + 1)
            seen[idx] = i
            res = max(res, i - l + 1)
        return res


# @lc code=end
