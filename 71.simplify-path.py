#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        s = deque()
        # n = len(path)
        # i = 0
        # while i < n:
        #     while i < n and path[i] == "/":
        #         i += 1
        #     j = i
        #     while j < n and path[j] != "/":
        #         j += 1
        #     if i < j:
        #         token = path[i:j]
        #         if token == "..":
        #             if s:
        #                 s.pop()
        #         elif token != ".":
        #             s.append(token)
        #     i = j
        for token in path.split("/"):
            if not token or token == ".":
                continue
            if token == "..":
                if s:
                    s.pop()
            else:
                s.append(token)
        return "/" + "/".join(s)


# @lc code=end
