#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        def count_palis(l, r):
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        for i in range(n):
            res += count_palis(i, i)
            res += count_palis(i, i + 1)
        return res


# @lc code=end
