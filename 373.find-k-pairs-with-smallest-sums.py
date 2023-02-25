#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
import heapq as hq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        hq.heapify(nums1)
        hq.heapify(nums2)
        min1 = hq.heappop(nums1)
        min2 = hq.heappop(nums2)
        res = [(min1, min2)]

        for _ in range(2, k + 1):
            if (nums1, nums2) == ([], []):
                return res
            if not nums2:
                res.append((hq.heappop(nums1), min2))
            elif not nums1 or nums1[0] > nums2[0]:
                res.append((min1, hq.heappop(nums2)))
            else:
                res.append((hq.heappop(nums1), min2))
        return res


# @lc code=end
