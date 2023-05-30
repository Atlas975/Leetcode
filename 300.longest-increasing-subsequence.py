#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#


# @lc code=start


from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [nums[0]] # BINARY SEARCH (PATIENCE SORTING)
        for num in nums[1:]:
            i = bisect_left(dp, num)
            if i == len(dp):  # num > all vals in LIS
                dp.append(num)
            else:  
                dp[i] = num  
        return len(dp)


# @lc code=end
