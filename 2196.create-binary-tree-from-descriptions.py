#
# @lc app=leetcode id=2196 lang=python3
#
# [2196] Create Binary Tree From Descriptions
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        n= len(descriptions)
        parents={desc[0]:None for desc in descriptions}
        root=None

        for i,desc in enumerate(descriptions):
            if desc[2]==1:
                if desc[0] in parents:



# @lc code=end

