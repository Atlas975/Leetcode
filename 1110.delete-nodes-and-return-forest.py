#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
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
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete = set(to_delete)
        q = deque([(root, True, root.val in to_delete)])

        while q:
            node, is_root, marked = q.popleft()
            if is_root and (not marked):
                res.append(node)
            if node.left:
                is_deleted = node.left.val in to_delete
                q.append((node.left, marked, is_deleted))
                if is_deleted:
                    node.left = None
            if node.right:
                is_deleted= node.right.val in to_delete
                q.append((node.right, marked, is_deleted))
                if is_deleted:
                    node.right = None

        return res

        # def dfs(node, is_root, marked):
        #     if is_root and (not marked):
        #         res.append(node)
        #     if node.left:
        #         is_deleted = node.left.val in to_delete
        #         dfs(node.left, marked, is_deleted)
        #         if is_deleted:
        #             node.left = None
        #     if node.right:
        #         is_deleted= node.right.val in to_delete
        #         dfs(node.right, marked, is_deleted)
        #         if is_deleted:
        #             node.right = None

        # dfs(root, True, root.val in to_delete)


# @lc code=end
