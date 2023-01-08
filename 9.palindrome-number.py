#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
from collections import deque


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s, q = deque(), deque()
        while x:
            lstdig = x % 10
            s.append(lstdig)
            q.appendleft(lstdig)
            x //= 10
        return s == q


# @lc code=end
