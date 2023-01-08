#
# @lc app=leetcode id=1344 lang=python3
#
# [1344] Angle Between Hands of a Clock
#

# @lc code=start
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = minutes * 6
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        diff = abs(minute_angle - hour_angle)
        return min(diff, 360 - diff)


# @lc code=end
