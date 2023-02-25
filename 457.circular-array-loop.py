#
# @lc app=leetcode id=457 lang=python3
#
# [457] Circular Array Loop
#

# @lc code=start
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        n = len(nums)
        moveto = {i: (i + nums[i]) % n for i in range(n)}
        inc = {k: v for k, v in moveto.items() if k != v}

        while inc:
            if any(k == v for k, v in inc.items()):
                return True

            inc = {k: moveto[v] for k, v in inc.items() if (nums[k] * nums[v] > 0) and (v in inc)}

        return False


# @lc code=end
