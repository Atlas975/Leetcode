#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # ITERATIVE
        # stack = deque([(p, q)])
        # while stack:
        #     p, q = stack.pop()
        #     if bool(p) ^ bool(q):
        #         return False
        #     if p:
        #         if p.val != q.val:
        #             return False
        #         stack.append((p.left, q.left))
        #         stack.append((p.right, q.right))
        # return True

        # RECURSIVE
        def check(p, q):
            if bool(p) ^ bool(q):
                return False
            if not p:
                return True
            if p.val != q.val:
                return False
            return check(p.left, q.left) and check(p.right, q.right)

        return check(p, q)


# @lc code=end
