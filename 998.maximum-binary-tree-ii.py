#
# @lc app=leetcode id=998 lang=python3
#
# [998] Maximum Binary Tree II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoMaxTree(
        self, root: Optional[TreeNode], val: int
    ) -> Optional[TreeNode]:
        if root and root.val > val:
            return TreeNode(val, root, None)
        if root.right and val > root.right.val:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root


# @lc code=end
