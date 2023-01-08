#
# @lc app=leetcode id=2309 lang=python3
#
# [2309] Greatest English Letter in Upper and Lower Case
#

# @lc code=start
class Solution:
    def greatestLetter(self, s: str) -> str:
        charset = set(s)
        return max((c.upper() for c in charset if c.swapcase() in charset), default="")


# @lc code=end
