#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
class Solution:

    def __init__(self) -> None:
        self.explored = {} 


    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        # n = len(points)
        # if len(points) == 1: return 0
        # res = 0
        # curr = 0 # select a random point as the starting point
        # dis = [math.inf] * n
        # explored = set()
        
        # for i in range(n - 1):
        #     x0, y0 = points[curr]
        #     explored.add(curr)
        #     for j, (x, y) in enumerate(points):
        #         if j in explored: continue
        #         dis[j] = min(dis[j], abs(x - x0) + abs(y - y0))
                
        #     delta, curr = min((d, j) for j, d in enumerate(dis)) 
        #     dis[curr] = math.inf
        #     res += delta
            
        # return res

        import math
        min_cost = 0
        
        for i in range(len(points)):
            
            rest = points[:i] + points[i+1:]
            cur_point = (points[i][0], points[i][1])

            print(f"Ref : {cur_point}, rest : {rest}")
            cur_min = self.findMin(points[i], rest)

            if cur_min != math.inf:
                min_cost += cur_min
        
            print(f"###### Min cost : {min_cost}")
        return min_cost

    def findMin(self,ref,points):
        import math
        min_dist = math.inf
        min_point = None
        for point in points:

            if (ref[0], ref[1]) in self.explored:
                continue
            dist = abs(ref[0]-point[0]) + abs(ref[1]-point[1])
            print(f"dist: {dist}")
            
            if dist < min_dist:
                min_dist = dist
                min_point = point
            print(f"Min dist: {min_dist}")

            if (min_point[0],min_point[1]) != (ref[0], ref[1]):
                self.explored[(min_point[0],min_point[1])] = True

        print(f"#########Ret min: {min_dist}")
        return min_dist


# @lc code=end

