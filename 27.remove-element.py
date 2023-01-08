#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newlen = 0
        for num in nums:
            if num != val:
                nums[newlen] = num
                newlen += 1
        return newlen


# @lc code=end
