#
# @lc app=leetcode id=1588 lang=python3
#
# [1588] Sum of All Odd Length Subarrays
#

# @lc code=start
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # res = 0; freq = 0; n = len(arr)
        # for i in range(n):
        #     onei=i+1
        #     freq = freq-(onei)//2+(n-onei)//2
        #     res += freq*arr[i]
        # return res

        res = 0
        freq = 0
        n = len(arr)
        for i in range(n):
            freq = freq - (i + 1) // 2 + (n - i + 1) // 2
            res += freq * arr[i]
        return res


# @lc code=end
