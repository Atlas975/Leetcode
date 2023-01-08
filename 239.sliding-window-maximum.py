#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res, dp = [], deque()
        l, r = 0, 0

        # for i,num in enumerate(nums):
        #     while dp and nums[dp[-1]]<num:
        #         dp.pop()
        #     dp.append(i)
        #     if dp[0] <= i - k:
        #         dp.popleft()
        #     if i >= k - 1:
        #         res.append(nums[dp[0]])
        # return res

        for i, num in enumerate(nums):
            while nums[r] < num:
                r -= 1
            r += 1
            if l <= i - k:
                l += 1
            if i >= k - 1:
                res.append(nums[l])
        return res


# @lc code=end
