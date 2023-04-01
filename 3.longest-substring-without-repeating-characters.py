#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = [None] * 128
        res, l = 0, 0

        for r, c in enumerate(s.encode()):
            if seen[c] is not None:
                l = max(l, seen[c] + 1)
            seen[c] = r
            res = max(res, r - l + 1)
        return res


# @lc code=end
