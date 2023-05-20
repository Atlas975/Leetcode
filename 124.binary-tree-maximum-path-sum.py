#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # ITERATIVE
        mxpath = float("-inf")
        gainmp = {}
        s = deque([(root, False)])

        while root or s:
            while root:
                s.append((root, False))
                root = root.left
            root, seen = s.pop()
            if not seen:
                s.append((root, True))
                root = root.right
                continue
            lgain = max(0, gainmp[root.left]) if root.left else 0
            rgain = max(0, gainmp[root.right]) if root.right else 0
            mxpath = max(mxpath, lgain + root.val + rgain)
            gainmp[root] = max(lgain, rgain) + root.val
            root = None
        return mxpath


        # RECURSIVE
        def dfs(node):
            if node is None:
                return 0
            lgain = lgain if (lgain := dfs(node.left)) > 0 else 0
            rgain = rgain if (rgain := dfs(node.right)) > 0 else 0
            self.mxsum = max(self.mxsum, lgain + node.val + rgain)
            return max(lgain, rgain) + node.val

        self.mxsum = root.val
        dfs(root)
        return self.mxsum


        # RECUSIVE NO GLOBAL
        def dfs(node):
            if node is None:
                return 0, float("-inf")
            lgain, lsum = dfs(node.left)
            rgain, rsum = dfs(node.right)

            mxsum = max(lsum, rsum, lgain + node.val + rgain)
            mxgain = max(lgain, rgain) + node.val
            return max(0, mxgain), mxsum
        return dfs(root)[1]






# @lc code=end
