#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
class MyStack:

    def __init__(self):
        self.q1 = []

    def push(self, x: int) -> None:
        self.q2 = [x]
        self.q2 += self.q1
        self.q1 = self.q2

    def pop(self) -> int:
        ret = self.q1[0]
        self.q1.pop(0)
        return ret

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        if not self.q1:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

