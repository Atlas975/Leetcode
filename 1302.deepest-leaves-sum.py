#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        res, stk = 0, deque([root])
        while stk:
            res = 0
            for _ in range(len(stk)):
                node = stk.popleft()
                res += node.val
                if node.left:
                    stk.append(node.left)
                if node.right:
                    stk.append(node.right)
        return res


# @lc code=end
