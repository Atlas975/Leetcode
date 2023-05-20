#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder = deque(preorder)
        inmap = {val: i for i, val in enumerate(inorder)}

        def build(l, r):
            if l > r:  # no nodes to left or right
                return None
            root = TreeNode(preorder.popleft())
            inloc = inmap[root.val] # index of root in inorder
            root.left, root.right = build(l, inloc - 1), build(inloc + 1, r)
            return root
        return build(0, len(inorder) - 1)


# @lc code=end
