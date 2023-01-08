#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)

        def valid_pali(l, r):
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
            return l >= r

        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                return valid_pali(i, n - i - 2) or valid_pali(i + 1, n - i - 1)
        return True


# @lc code=end
