#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 128
        res, mxfrq, l = 0, 0, 0

        for r, c in enumerate(s):
            freq[int(c)] += 1
            mxfrq = max(mxfrq, freq[int(c)])
            if r - l + 1 - mxfrq > k:
                freq[int(c)] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


# @lc code=end
