#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        res = targetSum - root.val
        if not (root.left or root.right):
            return res == 0
        return self.hasPathSum(root.left, res) or self.hasPathSum(root.right, res)

        # @lc code=end
