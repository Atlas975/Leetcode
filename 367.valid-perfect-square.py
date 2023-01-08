#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return False


# @lc code=end
