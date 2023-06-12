#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start


from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:  # too many or too few characters
            return False

        @cache
        def dfs(i, j):
            k = i + j # index in s3
            return (
                (i < n1 and s1[i] == s3[k] and dfs(i + 1, j))
                or (j < n2 and s2[j] == s3[k] and dfs(i, j + 1))
                or (k == n3) # successfullly interleaved
            )

        return dfs(0, 0)


# @lc code=end
