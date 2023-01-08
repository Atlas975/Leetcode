#
# @lc app=leetcode id=1566 lang=python3
#
# [1566] Detect Pattern of Length M Repeated K or More Times
#

# @lc code=start
from collections import defaultdict


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        prev = tuple(arr[:m])
        freq = 1

        for i in range(m, len(arr), m):
            curr = tuple(arr[i : i + m])
            if prev == curr:
                freq += 1
                if freq == k:
                    return True
            else:
                prev = curr
                freq = 1
        return False


# @lc code=end
