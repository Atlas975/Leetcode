#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        valid_pali= lambda s:(
            all(s[i]==s[-i] for i in range(len(s)//2))
        )


        def dfs(
        return res

# @lc code=end

