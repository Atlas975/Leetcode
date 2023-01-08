#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()[::-1]
        l = r = 0
        while r < len(s):
            r = s.find(" ", l)
            r = r if r != -1 else len(s)
            s = f"{s[:l]}{s[l:r][::-1]} {s[r:].lstrip()}"
            l = r = r + 1
        return s.rstrip()


# @lc code=end

# test with string "  hello world!  "
