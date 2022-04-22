#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet:

    def __init__(self):
        self.hashset = {}

    def add(self, key: int) -> None:
        self.hashset[key] = True

    def remove(self, key: int) -> None:
        try:
            del self.hashset[key]
        except KeyError: 
            pass

    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

