#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start


from collections import defaultdict


class Solution:
    def combinationSum2(self, cands: List[int], target: int) -> List[List[int]]:
        candMp = defaultdict(int)
        for c in cands:
            candMp[c] += 1
        keys = sorted(candMp.keys())
        res = []

        def dfs(remain, path, i):
            if remain == 0:
                res.append(path)
                return
            for j, cur in enumerate(keys[i:], i):
                if candMp[cur] == 0:
                    continue
                if cur > remain:
                    break
                candMp[cur] -= 1
                path.append(cur)
                dfs(remain - cur, path, j)
                path.pop()
                candMp[cur] += 1

        dfs(target, [], 0)
        return res

        # def dfs(i, path, pathsum):
        #     def search(num, j):
        #         if (npathsum := pathsum + num) == target:
        #             res.append(path + [num])
        #         elif npathsum < target and j < len(cands) - 1:
        #             dfs(j + 1, path + [num], npathsum)

        #     search(cands[i], i)
        #     for j in range(i + 1, len(cands)):
        #         if cands[j] != cands[j - 1]:
        #             search(cands[j], j)

        # res = []
        # cands.sort()
        # dfs(0, [], 0)
        # return res


# @lc code=end
