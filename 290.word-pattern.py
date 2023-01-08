#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1, d2 = {}, {}
        s_arr = s.split()
        if len(pattern) != len(s_arr):
            return False
        for v, w in zip(pattern, s_arr):
            if (v in d1 and d1[v] != w) or (w in d2 and d2[w] != v):
                return False
            d1[v], d2[w] = w, v
        return True

        # patlen=len(pattern)


# @lc code=endr
