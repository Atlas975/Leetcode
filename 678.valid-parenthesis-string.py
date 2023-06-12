#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#

# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        opmin = opmax = 0 # min/max number of open parens
        for c in s:
            match c:
                case "(": # 1 more open paren allowed
                    opmin += 1
                    opmax += 1
                case ")": # 1 less open paren allowed
                    if opmax == 0: # too many closing parens
                        return False
                    opmin = max(opmin - 1, 0) # ok, treat as empty string
                    opmax -= 1
                case _: # is *, can be either open or close or empty
                    opmin = max(opmin - 1, 0)
                    opmax += 1
        return opmin == 0
        
# @lc code=end

