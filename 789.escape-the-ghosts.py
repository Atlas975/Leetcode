#
# @lc app=leetcode id=789 lang=python3
#
# [789] Escape The Ghosts
#


# @lc code=start
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        tx, ty = target
        tdist = abs(tx) + abs(ty) # manhattan distance
        return all(
            tdist < (abs(gx - tx) + abs(gy - ty)) for gx, gy in ghosts
        )


# @lc code=end
