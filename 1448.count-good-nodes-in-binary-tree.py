#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
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
    def goodNodes(self, root: TreeNode) -> int:
        # ITERATIVE
        res = 0
        s = deque([(root, float('-inf'))])
        while s:
            node, maxVal = s.pop()
            if node.val >= maxVal:
                res += 1
                s.append((node.left, node.val)) if node.left else None
                s.append((node.right, node.val)) if node.right else None
            else:
                s.append((node.left, maxVal)) if node.left else None
                s.append((node.right, maxVal)) if node.right else None
        return res

        # RECURSIVE
        def check(node, maxVal):
            if node is None:
                return 0
            if node.val >= maxVal:
                return 1 + check(node.left, node.val) + check(node.right, node.val)
            return check(node.left, maxVal) + check(node.right, maxVal)
        return 1 + check(root.left, root.val) + check(root.right, root.val)


# @lc code=end˚
