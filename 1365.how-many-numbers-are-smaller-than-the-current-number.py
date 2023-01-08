#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#

# @lc code=start
from collections import defaultdict


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        cnt = {}
        for i, num in enumerate(sorted(nums)):
            if num not in cnt:
                cnt[num] = i

        return (cnt[num] for num in nums)


# @lc code=end
