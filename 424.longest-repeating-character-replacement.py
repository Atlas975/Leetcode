#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = defaultdict(int)
        longest, maxf, l = 0, 0, 0

        for r, c in enumerate(s):
            freq[c] += 1
            maxf = max(maxf, freq[c])
            if r - l + 1 - maxf > k:
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest


# @lc code=end
