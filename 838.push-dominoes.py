#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#

# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n, rpush = len(dominoes), -1
        res = list(dominoes)
        for hi, force in enumerate(dominoes):
            if force == "L":
                if rpush == -1:
                    for i in reversed(range(hi)):
                        if res[i] != ".":
                            break
                        res[i] = "L"
                else:
                    l, r = rpush + 1, hi - 1
                    while l < r:
                        res[l], res[r] = "R", "L"
                        l += 1
                        r -= 1
                    rpush = -1

            elif force == "R":
                if rpush != -1:
                    for j in range(rpush + 1, hi):
                        res[j] = "R"
                rpush = hi

        if rpush != -1:
            for j in range(rpush + 1, n):
                res[j] = "R"
        return "".join(res)


# @lc code=end
