#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        opmin = opmx = 0 # min/max number of open parens
        for c in s:
            match c:
                case "(": # 1 more open paren allowed
                    opmin += 1
                    opmx += 1
                case ")": # 1 less open paren allowed
                    if opmx == 0: # too many closing parens
                        return False
                    opmin = max(opmin - 1, 0)
                    opmx -= 1
                case "*": # can be either open or close
                    opmin = max(opmin - 1, 0)
                    opmx += 1
        return opmin == 0
        
# @lc code=end

