#
# @lc app=leetcode id=1041 lang=python3
#
# [1041] Robot Bounded In Circle
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        l_offset = {}
        r_offset = {}

        l_offset[(0,1)] = ()

        x,y = 0,0
        dir = "N"
        for ins in instructions:
            if ins == "G":
                y += 1
                if (x,y) not in visited:
                    visited.append()
                else:
                    return True
            elif ins == "R":
                
                    
            elif ins == "L":


        
# @lc code=end

