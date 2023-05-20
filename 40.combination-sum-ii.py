#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def bfs(cand, path, pathsum):
            n = len(cand)

            def search(num, i):
                if (npathsum := pathsum + num) == target:
                    res.append(path + [num])
                elif npathsum < target and (ncand := cand[i + 1 :]):
                    bfs(ncand, path + [num], npathsum)

            search(cand[0], 0)
            for i in range(1, n):
                if cand[i] != cand[i - 1]:
                    search(cand[i], i)

        res = []
        candidates.sort()
        bfs(candidates, [], 0)
        return res


# @lc code=end
