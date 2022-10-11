#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#

# @lc code=start

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # def dist(i,j):
        #     # BFS template?
        #     #queue
        #     q = [(i,j,0)]

        #     # set to keep track of visited items
        #     visited = set()

        #     # all the directions one can go from (i,j)
        #     dirs = [
        #         (1,0),
        #         (0,1),
        #         (-1,0),
        #         (0,-1)
        #     ]

        #     # while all the directions are covered

        #     while(q):
        #         for i in range(len(q)):
        #             x,y,d = q.pop(0)
        #             if mat[x][y] == 0:
        #                 return d
        #             visited.add((x,y))

        #             for dir in dirs:
        #                 new_x, new_y = x+dir[0], y+dir[1]
        #                 if new_x >= 0 and new_x <= len(mat)-1 \
        #                     and new_y >= 0 and new_y <= len(mat[0])-1:
        #                     if (new_x, new_y) not in visited:
        #                         q.append((new_x, new_y, d+1))

        #     return -1

        m,n = len(mat), len(mat[0])
        # ret = [[ 0 for x in range(n) ] for _ in range(m)]
        q = []
        visited = set()
        dirs = [
                (1,0),
                (0,1),
                (-1,0),
                (0,-1)
            ]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1

        while(q):
            x,y = q.pop(0)
            for dir in dirs:
                new_x, new_y = x+dir[0], y+dir[1]
                if new_x >= 0 and new_x <= len(mat)-1 and new_y >= 0 and new_y <= len(mat[0])-1 and mat[new_x][new_y] == -1:
                    mat[new_x][new_y] = mat[x][y]+1
                    visited.add((new_x, new_y))
                    q.append((new_x, new_y))

        return mat

       
                        
                             
                    

# @lc code=end

