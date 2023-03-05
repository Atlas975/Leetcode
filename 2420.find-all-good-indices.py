#
# @lc app=leetcode id=2420 lang=python3
#
# [2420] Find All Good Indices
#

# @lc code=start
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(k, len(nums) - k):
            left, right = i - k, i + 1
            while right < len(nums) and nums[right] >= nums[right - 1]:
                right += 1
            while left >= 0 and nums[left] <= nums[left + 1]:
                left -= 1
            if right - left - 1 >= 2 * k:
                res.append(i)
        return res

        # if isInc and 0 < l < len(nums) - k + 1:
        #     while (nums[l] <= nums[l - 1]) a
        #         l += 1


# @lc code=end
