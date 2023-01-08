#
# @lc app=leetcode id=1871 lang=python3
#
# [1871] Jump Game VII
#

# @lc code=start


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        i = 0
        n = len(s)
        while i < n - 1:
            if n - 1 <= i + maxJump:
                return True
            if i + maxJump < n and s[i + maxJump] == "0":
                i += maxJump
            elif i + minJump < n and s[i + minJump] == "0":
                i += minJump
            else:
                return False
        return True


# @lc code=end
