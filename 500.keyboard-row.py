#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows=(set('qwertyuiop'),set('asdfghjkl'),set('zxcvbnm'))

        res=[]
        for word in words:
            w=set(word.lower())
            if any(w.issubset(row) for row in rows):
                res.append(word)
        return res
    for 

# @lc code=end

