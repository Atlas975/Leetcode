#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r) -> int:
            if l > r:
                return -1
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    return binary_search(m + 1, r)
                else:
                    return binary_search(l, m - 1)
            if target < nums[m] or target > nums[r]:
                return binary_search(l, m - 1)
            return binary_search(m + 1, r)

        return binary_search(0, len(nums) - 1)


# @lc code=end
