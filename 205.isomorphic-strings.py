#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for v, w in zip(s, t):
            if (v in d1 and d1[v] != w) or (w in d2 and d2[w] != v):
                return False
            d1[v], d2[w] = w, v
        return True
        # return len(set(zip(s,t)))==len(set(s))==len(set(t))


# @lc code=end
