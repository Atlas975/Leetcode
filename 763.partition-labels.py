#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lstidx = [0] * 26
        for i, c in enumerate(s):
            lstidx[ord(c) - ord("a")] = i

        l, r = 0, 0
        for i, c in enumerate(s):
            r = max(r, lstidx[ord(c) - ord("a")])
            if i == r:
                res.append(r - l + 1)
                l = r + 1
        return res


# @lc code=end
