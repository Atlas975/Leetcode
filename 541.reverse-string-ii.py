#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # n = len(s)
        arr = list(s)
        for i in range(0, len(s), 2 * k):
            l, r = i, min(i + k - 1, len(s) - 1)

            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        return "".join(arr)


# @lc code=end
