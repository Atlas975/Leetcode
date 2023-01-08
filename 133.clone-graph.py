#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
# Definition for a Node.
from collections import defaultdict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        visited = {}

        def cloneNode(node):
            if node in visited:
                return visited[node]
            visited[node] = Node(node.val)
            visited[node].neighbors = list(map(cloneNode, node.neighbors))
            return visited[node]

        return cloneNode(node) if node else None


# @lc code=end
