#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        for l in range(n - 2):
            if l > 0 and nums[l - 1] == nums[l]:
                continue
            m, r = l + 1, n - 1
            while m < r:
                s = nums[l] + nums[m] + nums[r]
                if s < 0:
                    m += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[l], nums[m], nums[r]))
                    m += 1
                    while nums[m] == nums[m - 1] and m < r:
                        m += 1
        return res


# @lc code=end
