#
# @lc app=leetcode id=2288 lang=python3
#
# [2288] Apply Discount to Prices
#

# @lc code=start
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(" ")
        for i, word in enumerate(words[:]):
            if word[0] == "$":
                words[i] = f"${int(word[1:])*(100-discount)/100:.2f}"
        return " ".join(words)


# @lc code=end
