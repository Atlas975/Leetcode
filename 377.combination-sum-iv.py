#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#

# @lc code=start


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if target % num == 0:
                res += 1


# @lc code=end

# @lc code=end
