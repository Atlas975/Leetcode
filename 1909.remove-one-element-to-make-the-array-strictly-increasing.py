#
# @lc app=leetcode id=1909 lang=python3
#
# [1909] Remove One Element to Make the Array Strictly Increasing
#

# @lc code=start
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        for i, elem in enumerate(nums[:-1]):
            if elem >= nums[i + 1]:
                if i > 0 and nums[i + 1] > nums[i - 1]:
                    nums.pop(i)
                elif i == 0 and i + 2 < n:
                    if nums[i + 2] > nums[i + 1]:
                        nums.pop(i)
                    nums.pop(i)
                else:
                    nums.pop(i + 1)
                break

        if all(elem < nums[i + 1] for i, elem in enumerate(nums[:-1])):
            return True

        # return True


# @lc code=end
