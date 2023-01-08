#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
from collections import Counter
from string import ascii_lowercase


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        let_count = dict.fromkeys(ascii_lowercase, 0)
        s1_count = let_count | Counter(s1)
        s2_count = let_count | Counter(s2[:n1])
        matches = sum(s1_count[c] == s2_count[c] for c in ascii_lowercase)

        for r in range(n1, n2):
            if matches == 26:
                return True

            s2_count[s2[r]] += 1
            if s1_count[s2[r]] == s2_count[s2[r]]:
                matches += 1
            elif s1_count[s2[r]] + 1 == s2_count[s2[r]]:
                matches -= 1

            s2_count[s2[r - n1]] -= 1
            if s1_count[s2[r - n1]] == s2_count[s2[r - n1]]:
                matches += 1
            elif s1_count[s2[r - n1]] - 1 == s2_count[s2[r - n1]]:
                matches -= 1

        return matches == 26


# @lc code=end
