#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sn, tn = len(s), len(t)
        if tn > sn:
            return ""
        idx = lambda x: ord(x) - ord("A")
        res = (0, float("inf"))
        need = [0] * 58
        
        for c in map(idx, t):
            need[c] += 1
        l, needcnt = 0, len(t)

        for r, c in ((r, idx(c)) for r, c in enumerate(s)):
            if need[c] > 0: # c is in t, 1 less char to match
                needcnt -= 1
            need[c] -= 1

            if needcnt > 0: 
                continue
            while need[i := idx(s[l])] < 0: # remove preceding chars not needed
                need[i] += 1
                l += 1
            if r - l < res[1] - res[0]: 
                res = (l, r)

            need[idx(s[l])] += 1 # remove the first char in window
            needcnt += 1
            l += 1
        return s[res[0] : res[1] + 1] if res[1] != float("inf") else ""




# @lc code=end
