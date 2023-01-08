#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        n=len(words)
        word_lens=[len(word) for word in words]
        charmax=sum(word_lens)
        res=[]
        linelen=maxWidth
        currline=""
        idx_cache=[]
        if charmax <= linelen:
            return "".join(words)
        while words:
            currline+=words.pop(0)
            linelen=maxWidth-word_lens.pop(0)
            if words:





# @lc code=end

