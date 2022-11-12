#
# @lc app=leetcode id=1432 lang=python3
#
# [1432] Max Difference You Can Get From Changing an Integer
#

# @lc code=start
class Solution:
    def maxDiff(self, num: int) -> int:
        # Greedy
        mx, mn = float('-inf'), float('inf')
        num = str(num)

        for i in '0123456789':
            for j in '0123456789':
                next = num.replace(i,j)
                if next[0] == '0' or int(next) == 0:
                    continue
                mx = max(mx, int(next))
                mn = min(mn, int(next))

        return mx-mn
        
# @lc code=end

