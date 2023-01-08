#
# @lc app=leetcode id=2342 lang=python3
#
# [2342] Max Sum of a Pair With Equal Sum of Digits
#

# @lc code=start


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digmap, res = {}, -1
        for num in nums:
            dsum = sum(map(int, str(num)))
            if dsum not in digmap:
                digmap[dsum] = num
            else:
                res = max(res, digmap[dsum] + num)
                digmap[dsum] = max(digmap[dsum], num)
        return res


# @lc code=end
