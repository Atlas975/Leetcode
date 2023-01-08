#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1
        for num in nums:
            if num % 2 == 0:
                nums[even] = num
                even += 2
            else:
                nums[odd] = num
                odd += 2


# @lc code=end
