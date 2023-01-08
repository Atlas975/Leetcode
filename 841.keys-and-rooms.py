#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        locked = set(range(len(rooms)))

        def dfs(i):
            locked.remove(i)
            for key in rooms[i]:
                if key in locked:
                    dfs(key)

        dfs(0)
        return not locked


# @lc code=end
