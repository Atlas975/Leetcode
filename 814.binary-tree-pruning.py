#
# @lc app=leetcode id=814 lang=python3
#
# [814] Binary Tree Pruning
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.left:
            root.left = self.pruneTree(root.left)
        if root.right:
            root.right = self.pruneTree(root.right)
        return root if (root.left or root.right or root.val) else None


# @lc code=end
