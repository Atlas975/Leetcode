#
# @lc app=leetcode id=1899 lang=python3
#
# [1899] Merge Triplets to Form Target Triplet
#


# @lc code=start
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = 0
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue  # skip overszied triplets
            for i, v in enumerate(t):
                if target[i] == v:
                    res |= 1 << i
                    if res == 7: # all 3 bits are set
                        return True
        return False


# @lc code=end
