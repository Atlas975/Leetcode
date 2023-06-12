#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        frstidx = {}  # get first idx of each val, avoids duplicates
        for i, num in enumerate(nums[:-2]):
            if num not in frstidx:
                frstidx[num] = i

        for cur, l in frstidx.items():
            m, r = l + 1, n - 1
            while m < r:
                cursum = cur + nums[m] + nums[r]
                if cursum < 0:
                    m += 1
                elif cursum > 0:
                    r -= 1
                else:
                    res.append((cur, nums[m], nums[r]))
                    m += 1
                    while nums[m] == nums[m - 1] and m < r:
                        m += 1
        return res


# @lc code=end
