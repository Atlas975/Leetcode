#
# @lc app=leetcode id=2379 lang=python3
#
# [2379] Minimum Recolors to Get K Consecutive Black Blocks
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = cnt = blocks[:k].count("B")

        for i in range(k, len(blocks)):
            if blocks[i] == "B" and blocks[i - k] == "W":
                cnt += 1
            elif blocks[i] == "W" and blocks[i - k] == "B":
                cnt -= 1
            res = max(res, cnt)

        return k - res


# @lc code=end
