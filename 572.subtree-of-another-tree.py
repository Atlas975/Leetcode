#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.


from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def preord(node):
            return f"({node.val}{preord(node.left)}{preord(node.right)})" if node else "#"

        p, q = preord(root), preord(subRoot)
        return q in p


# @lc code=end
