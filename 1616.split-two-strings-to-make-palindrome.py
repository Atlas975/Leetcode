#
# @lc app=leetcode id=1616 lang=python3
#
# [1616] Split Two Strings to Make Palindrome
#

# @lc code=start
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        n = len(a)
        is_pali = lambda s: all(s[i] == s[-i - 1] for i in range(len(s) // 2))
        check = lambda a, b: next(
            (is_pali(a[i : n - i]) or is_pali(b[i : n - i]) for i in range(n // 2) if a[i] != b[-i - 1]),
            True,
        )
        return check(a, b) or check(b, a)


# @lc code=end
