#
# @lc app=leetcode id=2075 lang=python3
#
# [2075] Decode the Slanted Ciphertext
#

# @lc code=start
from itertools import product


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        res = ""
        for c, r in product(range(cols), range(rows)):
            idx = c + (r * (cols + 1))
            if idx >= n:
                break
            res += encodedText[idx]
        return res.rstrip(" ")


# @lc code=end
