#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []

        def dfs(i, path):
            if len(path) == k:
                comb.append(path)
                return
            for j in range(i, n + 1):
                dfs(j + 1, path + [j])

        dfs(1, [])
        return comb


# @lc code=end
