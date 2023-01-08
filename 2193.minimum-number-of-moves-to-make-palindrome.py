#
# @lc app=leetcode id=2193 lang=python3
#
# [2193] Minimum Number of Moves to Make Palindrome
#

# @lc code=start
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        n = len(s)

        def charswap(i, j):
            s = s

        l, r = 0, n - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue

            k = l + 1
            while k < r and s[k] != s[r]:
                k += 1

            ## swap s[l] with s[k]
            s


# @lc code=end
