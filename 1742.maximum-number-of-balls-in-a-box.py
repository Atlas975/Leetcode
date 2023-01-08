#
# @lc app=leetcode id=1742 lang=python3
#
# [1742] Maximum Number of Balls in a Box
#

# @lc code=start


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        res, buckets = 0, [0] * 46
        for i in range(lowLimit, highLimit + 1):
            dig_sum = sum(map(int, str(i)))
            buckets[dig_sum] += 1
            res = max(res, buckets[dig_sum])
        return res


# @lc code=end
