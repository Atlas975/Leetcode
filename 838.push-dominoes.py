#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#

# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n, l = len(dominoes), -1
        res = list(dominoes)
        for r, force in enumerate(dominoes):
            if force == "L":
                if l == -1:
                    for i in range(r - 1, -1, -1):
                        if res[i] != ".":
                            break
                        res[i] = "L"
                else:
                    i, j = l + 1, r - 1
                    while i < j:
                        res[i], res[j] = "R", "L"
                        i += 1
                        j -= 1
                    l = -1

            elif force == "R":
                if l != -1:
                    for i in range(l + 1, r):
                        res[i] = "R"
                l = r

        if l != -1:
            for i in range(l + 1, n):
                res[i] = "R"
        return "".join(res)


# @lc code=end
