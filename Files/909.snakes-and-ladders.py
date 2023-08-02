#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        need = {1:0}
        q = [1]

        for x in q:
            for i in range(x+1, x+7):
                a,b = (i-1)//n, (i-1)%n
                nxt = board[~a][b if a%2 == 0 else ~b]
                if nxt > 0: i = nxt
                if i == n*n: return need[x] + 1
                if i not in need:
                    need[i] = need[x] + 1
                    q.append(i)
        return -1
        
# @lc code=end

