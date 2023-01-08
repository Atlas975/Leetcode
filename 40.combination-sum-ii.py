#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def bfs(cand, path, path_sum):
            n = len(cand)

            def search(num, j):
                new_sum = path_sum + num
                if new_sum == target:
                    res.append(path + [num])
                elif new_sum < target and (arr := cand[j + 1 :]):
                    bfs(arr, path + [num], new_sum)

            search(cand[0], 0)
            for i in range(1, n):
                if cand[i] == cand[i - 1]:
                    continue
                search(cand[i], i)

        bfs(candidates, [], 0)
        return res


# @lc code=end
