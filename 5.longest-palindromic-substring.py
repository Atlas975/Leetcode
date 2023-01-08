#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""

        def exppali(l, r):
            nonlocal res
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            res = s[l + 1 : r] if r - l - 1 > len(res) else res

        for i in range(n):
            exppali(i, i)
            exppali(i, i + 1)
        return res


# @lc code=end
