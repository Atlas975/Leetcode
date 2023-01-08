#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q) -> "TreeNode":
        # ITERATIVE
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
        return None

        # RECURSIVE
        def check(node):
            if node.val < p.val and node.val < q.val:
                return check(node.right)
            elif node.val > p.val and node.val > q.val:
                return check(node.left)
            else:
                return node

        return check(root)


# @lc code=end
