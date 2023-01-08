#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return next(
            (
                next((i - j for j in range(i, -1, -1) if s[j].isspace()), i + 1)
                for i in range(len(s) - 1, -1, -1)
                if not s[i].isspace()
            ),
            0,
        )


# @lc code=end
