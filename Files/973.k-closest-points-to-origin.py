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
            if d not in hmap:                           # If d is not seen before, insert the point in a list
                hmap[d] = [point]
            else:
                hmap[d].append(point)                  # If d is already seen, add the point to the existing list
                    
        dists = sorted(hmap.keys())                    # Sort the keys/distances 

        i = 0
        while(i<k):
            if len(hmap[dists[i]]) > 1:                # If there are more than 1 point, add all of them to the response and increment i 
                for p in hmap[dists[i]]:
                    ret.append(p)
                    i+= 1
            else:
                ret.append(hmap[dists[i]][0])         # If there is only 1 element, add its first point.
                i += 1
                
        return ret

# @lc code=end

