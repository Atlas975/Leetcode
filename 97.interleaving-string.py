#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:  # too many or too few characters
            return False
        invalid = set()

        def dfs(i, j):
            if (i, j) in invalid: # invalid leaf node
                return False
            if (
                (i < n1 and s1[i] == s3[i + j] and dfs(i + 1, j))
                or (j < n2 and s2[j] == s3[i + j] and dfs(i, j + 1))
                or (i + j == n3)
            ):
                return True # no cache, result propagates up
            invalid.add((i, j))
            return False

        return dfs(0, 0)


# @lc code=end
