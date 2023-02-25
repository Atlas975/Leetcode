#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start


from collections import defaultdict
import heapq as hq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph = defaultdict(list)
        # for u, v, w in times:
        #     graph[u].append((v, w))

        # dist = {i: float("inf") for i in range(1, n + 1)}
        # dist[k] = 0
        # seen = [False] * (n + 1)

        # def dfs(node, elapsed):
        #     if seen[node]:
        #         return
        #     seen[node], dist[node] = True, min(dist[node], elapsed)
        #     for nei, d in graph[node]:
        #         dfs(nei, elapsed + d)

        # dfs(k, 0)
        # res = max(dist.values())
        # return res if res < float("inf") else -1

        # while True:
        #     cand_node = -1
        #     cand_dist = float("inf")
        #     for i in range(1, n + 1):
        #         if not seen[i] and dist[i] < cand_dist:
        #             cand_dist = dist[i]
        #             cand_node = i

        #     if cand_node < 0:
        #         break
        #     seen[cand_node] = True
        #     for nei, d in graph[cand_node]:
        #         dist[nei] = min(dist[nei], dist[cand_node] + d)
        # res = max(dist.values())
        # return res if res < float("inf") else -1

        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        # seen = [False] * (n + 1)
        dist = {}
        q = [(0, k)]

        while q:
            d, node = hq.heappop(q)
            if node in dist:
                continue
            seen[node] = True


# @lc code=end
