#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if all(s[k] == s[-k - 1] for k in range(n // 2)):
            return s
        self.res = s[0]  # at least 1 char

        def exppali(l, r):
            for _ in range(min(l + 1, n - r)):
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            if r - l - 1 > len(self.res):
                self.res = s[l + 1 : r]

        exppali(0, 1)  # even length
        for i in range(1, n - 1):
            exppali(i - 1, i + 1)  # odd length
            exppali(i, i + 1)  # even length
        return self.res



# @lc code=end
