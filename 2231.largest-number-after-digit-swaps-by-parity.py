#
# @lc app=leetcode id=2231 lang=python3
#
# [2231] Largest Number After Digit Swaps by Parity
#

# @lc code=start
import heapq


class Solution:
    def largestInteger(self, num: int) -> int:
        even_heap, odd_heap = [], []
        str_num = str(num)

        for c in str_num:
            if ord(c) % 2 == 0:
                heapq.heappush(even_heap, -int(c))
            else:
                heapq.heappush(odd_heap, -int(c))

        res = "".join(
            str(-heapq.heappop(even_heap)) if ord(c) % 2 == 0 else str(-heapq.heappop(odd_heap))
            for c in str_num
        )

        return int(res)


# @lc code=end
