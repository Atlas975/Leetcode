#
# @lc app=leetcode id=1247 lang=python3
#
# [1247] Minimum Swaps to Make Strings Equal
#

# @lc code=start
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y, y_x = 0, 0
        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                continue
            elif c1 == "x":
                x_y += 1
            else:
                y_x += 1

        if (x_y + y_x) % 2 == 1:
            return -1

        single_swaps = (x_y // 2) + (y_x // 2)  # xx, yy
        dual_swaps = (x_y % 2) * 2  # xy , yx

        return single_swaps + dual_swaps


# @lc code=end
