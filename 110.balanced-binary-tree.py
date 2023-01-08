#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # return self.check_balance(root)!=-1

        stack = deque([root])
        postorder = {}
        while stack and stack[-1]:
            node = stack[-1]
            if node.left and node.left not in postorder:
                stack.append(node.left)
            elif node.right and node.right not in postorder:
                stack.append(node.right)
            else:
                node = stack.pop()
                left_height = postorder.get(node.left, 0)
                if left_height == -1:
                    return False
                right_height = postorder.get(node.right, 0)
                if right_height == -1:
                    return False
                if abs(left_height - right_height) > 1:
                    return False
                postorder[node] = 1 + max(left_height, right_height)

        return True

    def check_balance(self, root):
        if root is None:
            return 0
        left = self.check_balance(root.left)
        right = self.check_balance(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)


# @lc code=end
