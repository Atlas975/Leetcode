#
# @lc app=leetcode id=1686 lang=python3
#
# [1686] Stone Game VI
#

# @lc code=start
import math
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        advantage=0
        turn=0
        rounds=len(aliceValues)-1
        game_states=math.factorial(rounds+1)
        for state in game_states:
            alicecpy=aliceValues
            bobcpy=bobValues
            for round in rounds:
                







            # tempcpy=bobValues[:]
            # for a,astone in enumerate(aliceValues):
            #     tempcpy.pop(a)
            #     advantage=max(advantage,astone-max(tempcpy))



        if advantage>0:
            return 1
        if advantage==0:
            return -1
        return 0


# @lc code=end

