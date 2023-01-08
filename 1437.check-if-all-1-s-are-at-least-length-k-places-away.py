#
# @lc app=leetcode id=1437 lang=python3
#
# [1437] Check If All 1's Are at Least Length K Places Away
#

# @lc code=start
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        n = len(nums)
        while i < n and nums[i] != 1:
            i += 1
        if i == n:
            return True
        cntr = 0
        for j in range(i + 1, n):
            if nums[j] == 1:
                if j - cntr - 1 < k:
                    return False
                cntr = j
        return True


# @lc code=end
