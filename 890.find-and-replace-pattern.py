#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#

# @lc code=start
from collections import Counter


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res=[]
        pcount=Counter(pattern)
        for word in words:


# @lc code=end

