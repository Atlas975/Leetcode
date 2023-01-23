#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        valid_pali= lambda s:(all(s[i]==s[-i] for i in range(len(s)//2)))


        def dfs(s, path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s)+1):
                if valid_pali(s[:i]):
                    dfs(s[i:], path+[s[:i]])
                    
        return res

# @lc code=end

