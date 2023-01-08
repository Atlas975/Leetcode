#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r"[^\w\s]", " ", paragraph).lower()
        pfreq = Counter(p for p in paragraph.split() if p not in banned)
        return max(pfreq, key=pfreq.get)

        # pcnt = [(-v, k) for k, v in pcnt.items()]
        # heapq.heapify(pcnt)
        # while pcnt:
        #     _, word = heapq.heappop(pcnt)
        #     if word not in banned:
        #         return word


# @lc code=end
