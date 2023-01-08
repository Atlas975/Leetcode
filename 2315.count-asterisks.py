#
# @lc app=leetcode id=2315 lang=python3
#
# [2315] Count Asterisks
#

# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:
        n = len(s)
        res = i = 0
        while i < n:
            if s[i] == "|":
                i += 1
                while i < n and s[i] != "|":
                    i += 1
            elif s[i] == "*":
                res += 1
            i += 1
        return res


# @lc code=end
