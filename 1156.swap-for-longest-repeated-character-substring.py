#
# @lc app=leetcode id=1156 lang=python3
#
# [1156] Swap For Longest Repeated Character Substring
#

# @lc code=start
from collections import Counter, defaultdict


class Solution:
    def maxRepOpt1(self, text: str) -> int:

        letcnt=Counter(text)
        window=defaultdict(int)
        l = maxf = 0
        for r,c in enumerate(text):
            window[c]+=1
            maxf=max(maxf,window[c])
            if r-l+1-maxf>1:
                window[text[l]]-=1
                l+=1
            elif



        maxlen,maxf,

# @lc code=end

