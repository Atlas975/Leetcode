#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sn,tn = len(s),len(t)
        if sn < tn: return ""
        scnt, window = Counter(s),defaultdict(int)

        start,end=0,float("inf")
        for r,c in enumerate(s):
            





# @lc code=end

