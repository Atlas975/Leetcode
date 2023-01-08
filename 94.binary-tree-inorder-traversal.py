#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)
            res.append(node.val)
            traverse(node.right)

        traverse(root)
        return res


# @lc code=end
