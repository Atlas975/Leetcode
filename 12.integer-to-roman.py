#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:

        mmap = ["", "M", "MM", "MMM"]
        cmap = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        xmap = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        imap = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return mmap[num // 1000] + cmap[(num % 1000) // 100] + xmap[(num % 100) // 10] + imap[num % 10]


# @lc code=end
