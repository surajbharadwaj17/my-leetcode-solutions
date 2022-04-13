from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        # find the index of the pivot
        n = len(nums)
        lo,hi = 0,n-1
        
        while(lo < hi):
            mid = (lo+hi)//2
            
            if nums[mid] > nums[hi]:
                lo = mid+1
            else:
                hi = mid
        
        rot = lo
        print(f'pivot point is {rot}')
        
        # Binary search accounting the rotation
        lo, hi = 0, n-1
        
        while(lo <= hi):
            mid = (lo+hi)//2
            real_mid = (mid+rot)%n
            
            if target == nums[real_mid]:
                return True
            
            if target > nums[real_mid]:
                lo = mid+1
            else:
                hi = mid-1
                
        return False


s = Solution()
l = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]

target = 2
print(s.search(l, target))
