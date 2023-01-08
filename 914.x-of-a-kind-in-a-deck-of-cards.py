#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#

# @lc code=start
from math import gcd


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        n = len(deck)
        if n < 2:
            return False

        card_count = {item: deck.count(item) for item in deck}
        mingcd = min(card_count.values())
        maxgcd = max(card_count.values())
        return all(
            gcd(num_card, mingcd) != 1 and gcd(num_card, maxgcd) != 1
            for num_card in card_count.values()
        )

        # return all(n%value==0 for value in card_count.values()) if n%types==0 else False


# @lc code=end
