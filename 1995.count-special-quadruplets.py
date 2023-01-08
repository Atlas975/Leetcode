#
# @lc app=leetcode id=1995 lang=python3
#
# [1995] Count Special Quadruplets
#

# @lc code=start
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n // 4):
            prev = float("-inf")
            total = 0
            for num in nums[i * 4 : i * 4 + 3]:
                if num < prev:
                    return False
                prev = num
                total += num
            if prev > nums[i * 4 + 3] or total != nums[i * 4 + 3]:
                return False
        return True


# @lc code=end
