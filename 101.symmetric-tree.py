#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check_symmetry(root.left, root.right) if root else root

    def check_symmetry(self, left, right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.check_symmetry(left.left, right.right) and self.check_symmetry(
            left.right, right.left
        )


# @lc code=end
