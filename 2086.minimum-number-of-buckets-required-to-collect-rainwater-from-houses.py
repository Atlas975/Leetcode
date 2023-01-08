#
# @lc app=leetcode id=2086 lang=python3
#
# [2086] Minimum Number of Buckets Required to Collect Rainwater from Houses
#

# @lc code=start
class Solution:
    def minimumBuckets(self, street: str) -> int:
        n = len(street)
        res = 0
        i = 0
        while i < n:
            if street[i] == "H":
                if i + 1 < n and street[i + 1] == ".":
                    res += 1
                    i += 2
                elif i >= 1 and street[i - 1] == ".":
                    res += 1
                else:
                    return -1
            i += 1
        return res


# @lc code=end
