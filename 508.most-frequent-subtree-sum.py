#
# @lc app=leetcode id=508 lang=python3
#
# [508] Most Frequent Subtree Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            totalfreq[total] += 1
            return total

        totalfreq = defaultdict(int)
        dfs(root)
        mxcnt = max(totalfreq.values())
        return (k for k, v in totalfreq.items() if v == mxcnt)


# @lc code=end
