#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        edges = defaultdict(list)
        for u, v in tickets:
            edges[u].append(v)
        for u in edges:  # less comparisons than full sort
            edges[u].sort(reverse=True)
        route = []

        # def dfs(u):
        #     while edges[u]:
        #         dfs(edges[u].pop())
        #     route.append(u)
        # dfs("JFK")

        
        s = deque(["JFK"])
        while s:
            while edges[s[-1]]:
                s.append(edges[s[-1]].pop())
            route.append(s.pop())
        return route[::-1]


# @lc code=end
