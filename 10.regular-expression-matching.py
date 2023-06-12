#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if j == -1:  # pattern is empty
                return i == -1  # string should be empty for a match
            if i == -1: # string is empty
                return p[j] == "*" and dfs(i, j - 2)  # a * can match 0 char

            if p[j] in (s[i], "."): 
                return dfs(i - 1, j - 1)
            if p[j] == "*":  # match 0, match 1+
                return dfs(i, j - 2) or (p[j - 1] in (s[i], ".") and dfs(i - 1, j))
            return False

        return dfs(len(s) - 1, len(p) - 1)
        # ns, np = len(s), len(p)

        # @cache
        # def dfs(i, j):
        #     if j == np:  # pattern is empty
        #         return i == ns  # check if pat covers whole string
        #     if i == ns:  # match empty string
        #         while j + 1 < np and p[j + 1] == "*":
        #             j += 2
        #         return j == np

        #     eql = (p[j] == ".") or (p[j] == s[i])
        #     if (j + 1 < np) and (p[j + 1] == "*"):
        #         return dfs(i, j + 2) or (eql and dfs(i + 1, j))  # match 0, match 1
        #     return eql and dfs(i + 1, j + 1)

        # return dfs(0, 0)


# @lc code=end

