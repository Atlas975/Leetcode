#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # ITERATIVE
        # s = deque([(root, float('-inf'), float('inf'))])
        # while s:
        #     node, lower, upper = s.pop()
        #     if node.val <= lower or node.val >= upper:
        #         return False
        #     if node.left:
        #         s.append((node.left, lower, node.val))
        #     if node.right:
        #         s.append((node.right, node.val, upper))
        # return True

        # RECURSIVE
        def dfs(node, l, r):
            if node is None:
                return True
            if node.val <= l or node.val >= r:
                return False
            return dfs(node.left, l, node.val) and dfs(node.right, node.val, r)

        return dfs(root, float("-inf"), float("inf"))


# @lc code=end
