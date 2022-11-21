#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ("+", "-", "*", "/")

        stack = []

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                #print(stack)
                if len(stack)>1:
                    n2, n1 = stack.pop(), stack.pop()
                    res = 0
                    if token == "+":
                        res = n1+n2
                    elif token == "-":
                        res = n1-n2
                    elif token ==  "*":
                        res = n1*n2
                    elif token == "/":
                        res = int(float(n1)/n2)
                    stack.append(res)
   
        return stack.pop()
        
# @lc code=end

