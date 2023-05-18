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

        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        bq, eq = deque([beginWord]), deque([endWord])
        bvis, evis = {beginWord}, {endWord}
        
        beginVisited = set()
        endVisited = set()
        beginVisited.add(beginWord)
        endVisited.add(endWord)
        
        wordParents = defaultdict(list)
        isForward = True
        isFound = False
        
        def backtrace(word, parents, path, results):
            if word == beginWord:
                results.append(path[::-1])
                return
            for parent in parents[word]:
                path.append(parent)
                backtrace(parent, parents, path, results)
                path.pop()
        
        def generateWords(word):
            words = []
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    newWord = word[:i] + char + word[i+1:]
                    if newWord != word and newWord in wordSet:
                        words.append(newWord)
            return words
        
        while beginQueue and endQueue:
            if len(beginQueue) > len(endQueue):
                beginQueue, endQueue = endQueue, beginQueue
                beginVisited, endVisited = endVisited, beginVisited
                isForward = not isForward
            
            size = len(beginQueue)
            for _ in range(size):
                currentWord = beginQueue.popleft()
                wordChars = list(currentWord)
                for i in range(len(wordChars)):
                    originalChar = wordChars[i]
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        wordChars[i] = char
                        transformedWord = ''.join(wordChars)
                        if transformedWord in endVisited:
                            isFound = True
                            if isForward:
                                wordParents[currentWord].append(transformedWord)
                            else:
                                wordParents[transformedWord].append(currentWord)
                        if transformedWord not in beginVisited and transformedWord in wordSet:
                            if isForward:
                                wordParents[currentWord].append(transformedWord)
                            else:
                                wordParents[transformedWord].append(currentWord)
                            beginQueue.append(transformedWord)
                            beginVisited.add(transformedWord)
                    wordChars[i] = originalChar
            
            if isFound:
                break
        
        results = []
        backtrace(endWord, wordParents, [endWord], results)
        return results


# @lc code=end
