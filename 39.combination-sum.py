#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def bfs(cand, path, path_sum):
            for i, num in enumerate(cand):
                new_sum = path_sum + num
                if new_sum == target:
                    res.append(path + [num])
                elif new_sum < target:
                    bfs(cand[i:], path + [num], new_sum)

        bfs(candidates, [], 0)
        return res


# @lc code=end
