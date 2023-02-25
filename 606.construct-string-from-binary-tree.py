#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        if root.left and root.right:
            return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"

        if root.left:
            return f"{root.val}({self.tree2str(root.left)})"

        return f"{root.val}()({self.tree2str(root.right)})" if root.right else str(root.val)


# @lc code=end
