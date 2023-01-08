#
# @lc app=leetcode id=2177 lang=python3
#
# [2177] Find Three Consecutive Integers That Sum to a Given Number
#

# @lc code=start
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3:
            return []
        mid = num // 3
        return [mid - 1, mid, mid + 1]


# @lc code=end
\
