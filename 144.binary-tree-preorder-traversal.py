#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # def traverse(node):
        #     if not node:
        #         return
        #     res.append(node.val)
        #     traverse(node.left)
        #     traverse(node.right)
        # traverse(root)

        if root is None:
            return res
        s = deque([root])
        while s:
            node = s.pop()
            res.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)

        return res


# @lc code=end
