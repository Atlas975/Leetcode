#
# @lc app=leetcode id=2303 lang=python3
#
# [2303] Calculate Amount Paid in Taxes
#

# @lc code=start
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        res = prev = 0
        for bracket in brackets:
            if income < bracket[0]:
                res += (income - prev) * (bracket[1] / 100)
                return res
            else:
                res += (bracket[0] - prev) * (bracket[1] / 100)
                prev = bracket[0]
        return res


# @lc code=end
