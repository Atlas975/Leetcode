#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        sgrps = s.lower().split("-")
        postfix = ''.join(sgrps[1:])
        for c in
        for c in "".join(sgrps)[1:]:
            if len(postfix) == k:
                postfix += "-"


# @lc code=end

