#
# @lc app=leetcode id=1941 lang=python3
#
# [1941] Check if All Characters Have Equal Number of Occurrences
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1
        base = freq[s[0]]
        return all(freq[c] == base for c in s)


# @lc code=end
