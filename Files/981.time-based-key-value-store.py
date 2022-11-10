#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
import collections 
class TimeMap:

    def __init__(self):
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.map[key])

        while left < right:
            mid = (left+right)//2
            if self.map[key][mid][1] <= timestamp:
                left = mid+1
            elif self.map[key][mid][1] > timestamp:
                right = mid

        if right == 0:
            return ""
        else:
            return self.map[key][right-1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

