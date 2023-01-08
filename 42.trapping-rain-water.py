#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start


class Solution:
    def trap(self, height: List[int]) -> int:
        def helper(lmax, rmax, l, r):
            return (
                (lmax - height[l + 1] + helper(lmax, rmax, l + 1, r))
                if lmax > height[l + 1]
                else helper(height[l + 1], rmax, l + 1, r)
                if lmax < rmax
                else rmax - height[r - 1] + helper(lmax, rmax, l, r - 1)
                if rmax > height[r - 1]
                else helper(lmax, height[r - 1], l, r - 1)
                if l < r
                else 0
            )

        l, r = 0, len(height) - 1
        return helper(height[l], height[r], l, r)


# @lc code=end
