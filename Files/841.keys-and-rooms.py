#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room):
            if room not in visited:
                visited.add(room)
                for key in rooms[room]:
                    dfs(key)

        dfs(0)

        return len(rooms) == len(visited)
        
# @lc code=end

