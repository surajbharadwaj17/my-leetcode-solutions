#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = board
        cols = []
        boxes = []
        m,n = len(board), len(board[0])

        # Column elements
        for i in range(n):
            t = []
            for j in range(m):
                t.append(board[j][i])
            cols.append(t)


        # 3*3 box elements
        for i in range(0,m,3):
            for j in range(0,n,3):
                t = []
                for p in range(i, i+3):
                    for q in range(j, j+3):
                        t.append(board[p][q])
            boxes.append(t)

        if self._is_valid(rows) and self._is_valid(cols) and self._is_valid(boxes):
            return True
        else:
            return False


    def _is_valid(self, l:List[List[str]]):

        for ele in l:
            hmap = {}
            for sub in ele:
                try:
                    #if sub.isdigit():
                    if int(sub) < 0 or int(sub) > 10 :
                        return False
                    else:
                        if int(sub) in hmap:
                            return False
                        else:
                            hmap[int(sub)] = 1
                except:
                    continue
        
        return True

        
# @lc code=end

