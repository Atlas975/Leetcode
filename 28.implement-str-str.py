#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        sublen = len(needle)
        strlen = len(haystack)

        if sublen == 0 or sublen > strlen:
            return -1
        for i in range(strlen - sublen + 1):
            if haystack[i : i + sublen] == needle:
                return i
        return -1


# @lc code=end
