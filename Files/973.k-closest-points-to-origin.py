#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hmap = {}
        ret = []
        
        for point in points:
            d = sqrt((point[0])**2 + (point[1])**2)
            if d not in hmap:
                hmap[d] = [point]
            else:
                hmap[d].append(point)
                    
        dists = sorted(hmap.keys())

        for i in range(k):
            if len(hmap[dists[i]]) > 1:
                for p in hmap[dists[i]]:
                    ret.append(p)
            else:
                ret.append(hmap[dists[i]][0])
                
        return ret

# @lc code=end

