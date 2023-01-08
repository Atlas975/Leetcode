#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        rmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return (
            sum(
                -rmap[c] if rmap[c] < rmap[s[i + 1]] else rmap[c]
                for i, c in enumerate(s[:-1])
            )
            + rmap[s[-1]]
        )


# @lc code=end
