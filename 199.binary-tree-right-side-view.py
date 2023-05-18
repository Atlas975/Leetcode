#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # RECURSIVE
        def r_search(node, level):
            if node is None:
                return
            if level == len(res):
                res.append(node.val)
            r_search(node.right, level + 1) # right first
            r_search(node.left, level + 1)
        r_search(root, 0)
        return res

        # ITERATIVE
        if root is None:
            return []
        q = deque([root])
        while q:
            for node in (q.popleft() for _ in range(len(q) - 1)): 
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None
            rightSide = q.popleft()
            q.append(rightSide.left) if rightSide.left else None
            q.append(rightSide.right) if rightSide.right else None
            res.append(rightSide.val)
        return res


# @lc code=end
