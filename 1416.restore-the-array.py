#
# @lc app=leetcode id=1416 lang=python3
#
# [1416] Restore The Array
#

# @lc code=start


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        kn, sn = len(str(k)), len(s)
        dp = [1] * (sn + 1)

        for i in range(sn):
            res, cur = 0, ""

            for j in range(i, max(-1, i - kn), -1):
                cur = s[j] + cur
                if cur[0] != "0" and int(cur) <= k:
                    res += dp[j]

            if res == 0:
                return 0
            else:
                dp[i + 1] = res % (10**9 + 7)

        return dp[-1]


# @lc code=end
