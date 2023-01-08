#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
from collections import defaultdict


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # res = []
        # nums1.sort()
        # nums2.sort()
        # n1, n2 = len(nums1), len(nums2)
        # i, j = 0, 0
        # while i<n1 and j<n2:
        #     if nums1[i] < nums2[j]:
        #         i += 1
        #     elif nums1[i] > nums2[j]:
        #         j += 1
        #     else:
        #         if not res or nums1[i] != res[-1]:
        #             res.append(nums1[i])
        #         i += 1
        #         j += 1
        # return res

        res, occur = [], defaultdict(int)
        for num in nums1:
            occur[num] += 1
        for num in nums2:
            if occur[num]:
                res.append(num)
                occur[num] = 0
        return res


# @lc code=end
