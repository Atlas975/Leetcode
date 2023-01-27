#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        lett = {}
        for i, c in enumerate(s):
            lett[c] = i

        l, r = 0, 0
        for i, c in enumerate(s):
            r = max(r, lett[c])
            if i == r:
                res.append(r - l + 1)
                l = r + 1
        return res


# @lc code=end
