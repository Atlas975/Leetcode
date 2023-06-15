#
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#


# @lc code=start
class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        n = len(s)
        s = list(s)
        shiftcnt = sum(shifts)
        for i in range(n):
            val = (ord(s[i]) - 97 + shiftcnt) % 26
            s[i] = chr(97 + val)
            shiftcnt -= shifts[i]
        return "".join(s)


# @lc code=end
