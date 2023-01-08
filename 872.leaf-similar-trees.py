#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.get_leaves(root1) == self.get_leaves(root2)

    def get_leaves(self, root) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        return self.get_leaves(root.left) + self.get_leaves(root.right)


# @lc code=end
