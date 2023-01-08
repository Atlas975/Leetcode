#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # self.inverse(root) #recursive sol
        stack = deque([root])
        while stack:
            node = stack.pop()
            if node is None:
                continue
            stack.append(node.left)
            stack.append(node.right)
            node.left, node.right = node.right, node.left

        def inverse(root):
            if root is None:
                return
            inverse(root.left)
            inverse(root.right)
            root.left, root.right = root.right, root.left

        inverse(root)
        return root


# @lc code=end
