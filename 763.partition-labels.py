#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        l, r = 0, 0
        res = []

        for i, c in enumerate(s):
            r = max(r, last[c])
            if r == i:
                res.append(r - l + 1)
                l = r + 1

        return res


# @lc code=end
