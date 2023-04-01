#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        res = r = l = 0
        lastidx = len(nums) - 1

        while r < lastidx:
            l, r = r + 1, max(i + nums[i] for i in range(l, r + 1))
            res += 1
        return res


# @lc code=end
