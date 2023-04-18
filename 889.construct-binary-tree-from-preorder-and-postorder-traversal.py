#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:


        self.pre, self.pos = 0, 0 

        def rebuild(root):
            self.pre += 1
            if root.val != postorder[self.pos]:
                root.left = rebuild(TreeNode(preorder[self.pre]))
            if root.val != postorder[self.pos]:
                root.right = rebuild(TreeNode(preorder[self.pre]))
            self.pos += 1
            return root

        return rebuild(TreeNode(preorder[self.pre]))
        
        
# @lc code=end

