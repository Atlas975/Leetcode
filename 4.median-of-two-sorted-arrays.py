#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        INF, NEG_INF = float("inf"), float("-inf")
        nA, nB = len(nums1), len(nums2)
        total = nA + nB
        half = total // 2
        l, r = 0, nB

        while l <= r:
            mB = (l + r) // 2
            mA = half - mB

            lA = nums1[mA - 1] if (mA != 0) else NEG_INF
            rA = nums1[mA] if (mA != nA) else INF
            lB = nums2[mB - 1] if (mB != 0) else NEG_INF
            rB = nums2[mB] if (mB != nB) else INF

            if lA > rB:
                l = mB + 1
            elif lB > rA:
                r = mB - 1
            else:  # lA <= rB and lB <= rA
                midr = min(rA, rB)
                return midr if total % 2 else (midr + max(lA, lB)) / 2
        return -1


# @lc code=end
