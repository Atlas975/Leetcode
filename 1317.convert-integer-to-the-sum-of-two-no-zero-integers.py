#
# @lc app=leetcode id=1317 lang=python3
#
# [1317] Convert Integer to the Sum of Two No-Zero Integers
#

# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return next(
            (
                [i, n - i]
                for i in range(1, n)
                if "0" not in str(i) and "0" not in str(n - i)
            ),
            [],
        )


# @lc code=end
