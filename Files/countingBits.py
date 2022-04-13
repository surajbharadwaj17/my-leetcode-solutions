"""
Given an integer n, return an array ans of length n + 1 
such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.


Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

"""

class Solution:
    def countBits(self, n) -> list[int]:
        import collections

        ret = [0] * (n+1)

        for i in range(n+1):
            bn = bin(i)

            count = collections.Counter(bn)

            ret[i] = count['1']

        return ret

soln = Solution()
n = 5

print(soln.countBits(n))