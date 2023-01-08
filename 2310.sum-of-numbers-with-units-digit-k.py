#
# @lc app=leetcode id=2310 lang=python3
#
# [2310] Sum of Numbers With Units Digit K
#

# @lc code=start
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        unitdig = num % 10
        for i in range(1, 11):
            kmult = k * i
            if kmult > num:
                return -1
            if kmult % 10 == unitdig:
                return i
        return -1


# @lc code=end
