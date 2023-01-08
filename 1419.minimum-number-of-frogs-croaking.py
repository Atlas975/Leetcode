#
# @lc app=leetcode id=1419 lang=python3
#
# [1419] Minimum Number of Frogs Croaking
#

# @lc code=start

from collections import defaultdict


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        n = len(croakOfFrogs)
        if n % 5 != 0:
            return -1

        # baselen=len(croakhash['c'])

        # for letter in 'roak':
        #     if len(croakhash[letter]) != baselen:
        #         return -1

        # oneforg=False

        # for i in range(baselen):
        #     if all(croakhash[letter][i] < croakhash[letter][i+1] for letter in 'croak'[:-2]):
        #         oneforg=True
        #     if any(croakhash[croak[j]][i]>croakhash[croak[j+1]][i] for j in range(4)):
        #         return -1
        # if oneforg:
        #     return 1
        # return baselen


# @lc code=end
