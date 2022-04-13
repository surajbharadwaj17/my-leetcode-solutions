class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mySet = []
        

    def add(self, key: int) -> None:
        if key not in self.mySet:
            self.mySet.append(key)
        


    def remove(self, key: int) -> None:
        try:
            self.mySet.remove(key)
        except:
            pass
        
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        try:
            if key in self.mySet:
                return True
        except:
            return False
      

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)