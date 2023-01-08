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
        def check(root1, root2):
            if bool(root1) ^ bool(root2):
                return False
            if root1:
                if root1.val != root2.val:
                    return False
                lcheck = check(root1.left, root2.left)
                rcheck = check(root1.right, root2.right)
                return lcheck and rcheck
            return True

        def is_subtree(root, subRoot):
            if check(root, subRoot):
                return True
            if root.left and is_subtree(root.left, subRoot):
                return True
            return bool(root.right and is_subtree(root.right, subRoot))

        return is_subtree(root, subRoot)


# @lc code=end
