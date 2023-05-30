import heapq
from itertools import chain


def alienOrder(words: list[str]) -> str:
    def topological_sort(graph):
        inlinks = {u: 0 for u in graph}
        for vertices in graph.values():
            for v in vertices:
                inlinks[v] += 1
        pq = [u for u in graph if inlinks[u] == 0]
        heapq.heapify(pq) # sorts in normal lexical order if multiple roots
        res = []

        while pq:
            u = heapq.heappop(pq)
            res.append(u)
            for v in graph[u]:
                inlinks[v] -= 1
                if inlinks[v] == 0:
                    heapq.heappush(pq, v)
        return "".join(res) if len(res) == len(graph) else ""

    graph = {c : [] for c in chain(*words)}
    for w1, w2 in ((words[i], words[i + 1]) for i in range(len(words) - 1)):
        ordinal = False
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                graph[c1].add(c2)
                ordinal = True
                break
        if not ordinal and len(w1) > len(w2):
            return ""
    return topological_sort(graph)


# ["zy","zx"]

print(alienOrder(["zy", "zx"]))
