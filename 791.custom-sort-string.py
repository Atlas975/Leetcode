#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#
# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        ans = []
        for c in order:
            ans.append(c * cnt[c])
            del cnt[c]
        ans.extend(c * v for c, v in cnt.items())
        return "".join(ans)


# @lc code=end
