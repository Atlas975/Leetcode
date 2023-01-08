#
# @lc app=leetcode id=1898 lang=python3
#
# [1898] Maximum Number of Removable Characters
#

# @lc code=start
from collections import Counter


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        s_count = Counter(s)
        p_count = Counter(p)
        res = 0
        for i in removable:
            if s[i] in p_count:
                if s_count[s[i]] >= p_count[s[i]]:
                    res += 1
                    s_count[s[i]] -= 1
            else:
                res += 1
        return res


# @lc code=end
