#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#

# @lc code=start


from collections import deque


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        # def backtrack(sub="", i=0):
        #     if len(sub)==n:
        #         res.append(sub)
        #     elif s[i].isdigit():
        #         backtrack(sub+s[i], i+1)
        #     else:
        #         backtrack(sub+s[i].swapcase(), i+1)
        #         backtrack(sub+s[i],i+1)
        # backtrack()

        res = []
        stack = deque([("", 0)])
        n = len(s)

        while stack:
            sub, i = stack.pop()
            if len(sub) == n:
                res.append(sub)
            elif s[i].isdigit():
                stack.append((sub + s[i], i + 1))
            else:
                stack.append((sub + s[i].swapcase(), i + 1))
                stack.append((sub + s[i], i + 1))

        return res


# @lc code=end
