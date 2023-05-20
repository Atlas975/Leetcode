#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start
from collections import defaultdict, deque
from string import ascii_lowercase
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        size = len(wordList[0])
        adjs = dict()
        visited = set()
        for word in wordList:
            for i in range(size):
                key = word[0:i] + "*" + word[i + 1 : size]
                if key in adjs:
                    adjs[key].append(word)
                else:
                    # adjs[key] = [word]

        # q = deque()
        q.append(beginWord)
        visited.add(beginWord)

        check = False
        l_stack = []

        while q and not check:
            q_size = len(q)

            temp = set()
            for _ in range(q_size):
                word = q.popleft()
                temp.add(word)

                for i in range(size):
                    key = word[0:i] + "*" + word[i + 1 : size]
                    if key in adjs:
                        for neighbor in adjs[key]:
                            if neighbor == endWord:
                                check = True
                            if neighbor not in visited:
                                q.append(neighbor)
                                visited.add(neighbor)
                            else:
                                pass
            l_stack.append(temp)

        if not check:
            return []

        l_size = len(l_stack)

        final = []
        k = l_size - 1
        cand = l_stack[k]
        for i in range(size):
            key = endWord[0:i] + "*" + endWord[i + 1 : size]
            if key in adjs:
                for neighbor in adjs[key]:
                    if neighbor in cand:
                        final.append([neighbor, endWord])
        for i in range(1, l_size):
            k = l_size - 1 - i
            temp_dict = {}
            l_f = len(final)
            cand = l_stack[k]

            for j in range(l_f):
                path = final.pop()
                word = path[0]
                if k > 0:
                    if word in temp_dict:
                        keys = temp_dict[word]
                        for key in keys:
                            final.insert(0, [key] + path)
                    else:
                        temp_dict[word] = []

                        for i in range(size):
                            key = word[0:i] + "*" + word[i + 1 : size]
                            if key in adjs:
                                for neighbor in adjs[key]:
                                    if neighbor in cand:
                                        temp_dict[word].append(neighbor)
                                        final.insert(0, [neighbor] + path)
                else:
                    final.insert(0, [beginWord] + path)

        return final

        # word_set, reverse = set(wordList), False
        # res = []
        # if endWord not in word_set:
        #     return []
        # bq, eq = deque([(beginWord, [beginWord])]), deque([(endWord, [endWord])])
        # bpos, epos = {beginWord: [beginWord]}, {endWord: [endWord]}

        # while bq and eq:
        #     for path, st, c, en in (
        #         (path, w[:i], c, w[i + 1 :])
        #         for w, path in (bq.popleft() for _ in range(len(bq)))
        #         for i, c in enumerate(w)
        #     ):
        #         for nw in (st + l + en for l in ascii_lowercase if l != c):
        #             if epath := epos.get(nw):
        #                 res.append(epath + path[::-1] if reverse else path + epath[::-1])
        #             elif nw in word_set:
        #                 new_path = path + [nw]
        #                 bpos[nw] = new_path
        #                 bq.append((nw, new_path))
        #                 word_set.remove(nw)
        #     if res:
        #         return res
        #     if len(bq) > len(eq):
        #         bq, bpos, eq, epos = eq, epos, bq, bpos
        #         reverse = not reverse
        # return res

        # Use bidirectional BFS to find the shortest path


# @lc code=end
