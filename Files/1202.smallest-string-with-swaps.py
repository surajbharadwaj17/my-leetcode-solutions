#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#

# @lc code=start
from collections import defaultdict


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        class UnionFind:
            def __init__(self,n) -> None:
                self.parent = list(range(n))

            def union(self, x,y):
                self.parent[self.find(y)] = self.find(x)

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

        n = len(s)
        UF = UnionFind(n)
        ret = ""
        d = defaultdict(list)

        for (x,y) in pairs:
            UF.union(x,y)

        for i in range(n):
            d[UF.find(i)].append(s[i])

        for key in d:
            d[key].sort(reverse= True)

        for i in range(n):
            ret += d[UF.find(i)].pop()

        return ret



        
# @lc code=end

