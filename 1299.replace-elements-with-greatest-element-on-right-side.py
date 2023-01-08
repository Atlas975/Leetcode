#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr[-1], mxr = -1, arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            arr[i], mxr = mxr, max(mxr, arr[i])
        return arr


# @lc code=end
