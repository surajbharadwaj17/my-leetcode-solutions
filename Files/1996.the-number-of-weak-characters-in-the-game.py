#
# @lc app=leetcode id=1996 lang=python3
#
# [1996] The Number of Weak Characters in the Game
#

# @lc code=start
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # cnt = 0
        # for i in range(len(properties)):
        #     print(properties[i])
        #     rest = properties[:i] + properties[i+1:]
        #     print(rest)
        #     for j in range(len(rest)):
        #         if properties[j][0] > properties[i][0] and properties[j][1] > properties[i][1]:
        #             cnt += 1
        # return cnt

        cnt, mtn = 0,0
        properties = sorted(properties, key=lambda x: (-x[0], x[1]))

        for a,d in properties:
            if d < mtn:
                cnt += 1
            else:
                mtn = d
        return cnt

        # for i in range(len(properties)):
        #     if properties[i][1] < mtn:
        #         cnt += 1
        #     mtn = min(mtn, properties[i][1])
        # return cnt


        
# @lc code=end

