#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#
# https://leetcode.com/problems/maximum-frequency-stack/description/
#
# algorithms
# Hard (64.80%)
# Likes:    2549
# Dislikes: 43
# Total Accepted:    94.1K
# Total Submissions: 144.8K
# Testcase Example:  '["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]\n' +
  '[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]'
#
# Design a stack-like data structure to push elements to the stack and pop the
# most frequent element from the stack.
# 
# Implement the FreqStack class:
# 
# 
# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the
# stack.
# 
# If there is a tie for the most frequent element, the element closest to the
# stack's top is removed and returned.
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop",
# "pop", "pop"]
# [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
# Output
# [null, null, null, null, null, null, null, 5, 7, 5, 4]
# 
# Explanation
# FreqStack freqStack = new FreqStack();
# freqStack.push(5); // The stack is [5]
# freqStack.push(7); // The stack is [5,7]
# freqStack.push(5); // The stack is [5,7,5]
# freqStack.push(7); // The stack is [5,7,5,7]
# freqStack.push(4); // The stack is [5,7,5,7,4]
# freqStack.push(5); // The stack is [5,7,5,7,4,5]
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes
# [5,7,5,7,4].
# freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is
# closest to the top. The stack becomes [5,7,5,4].
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes
# [5,7,4].
# freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is
# closest to the top. The stack becomes [5,7].
# 
# 
# 
# Constraints:
# 
# 
# 0 <= val <= 10^9
# At most 2 * 10^4 calls will be made to push and pop.
# It is guaranteed that there will be at least one element in the stack before
# calling pop.
# 
# 
#

# @lc code=start
class FreqStack:

    def __init__(self):
      import collections
      self.stack = collections.defaultdict(list)
      self.freq = collections.Counter()
      self.max_f = 0

    def push(self, val: int) -> None:
      
      self.freq[val] += 1
      self.stack[self.freq[val]].append(val)
      self.max_f = max(self.max_f, self.freq[val])

    def pop(self) -> int:
        
      p = self.stack[self.max_f].pop()

      if not self.stack[self.max_f]:
        self.max_f = self.max_f - 1

      self.freq[p] -= 1

      return p



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

