#
# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        l, m = 0, n // 2
        while l < m and palindrome[l] == "a":
            l += 1
        if l != m:
            return f"{palindrome[:l]}a{palindrome[l + 1:]}"
        return f"{palindrome[:-1]}b" if n > 1 else ""


# @lc code=end
