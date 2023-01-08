#
# @lc app=leetcode id=1855 lang=python3
#
# [1855] Maximum Distance Between a Pair of Values
#

# @lc code=start
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = mxdist = 0
        j = 1
        n1, n2 = len(nums1), len(nums2)
        while i < n1 and j < n2:
            if nums1[i] > nums2[j]:
                i += 1
                j = max(i + 1, j)
            else:
                mxdist = max(mxdist, j - i)
                j += 1
        return mxdist


# @lc code=end
