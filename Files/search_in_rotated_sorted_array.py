from typing import List

class Solution:
    #### Approach 1 (time limit exceeded) ####
    # def search(self, nums: List[int], target: int) -> int:
    
    #     if len(nums) ==1:
    #         if target == nums[0]:
    #             return 0
    #         else:
    #             return -1
    #     if len(nums) ==2:
    #         if target == nums[0]:
    #             return 0
    #         elif target == nums[1]:
    #             return 1
    #         else:
    #             return -1
        
    #     # find the pivot
    #     n = len(nums)
    #     p = n//2
        
    #     while((p<n) and (p>=0)):            
    #         if ( (nums[p-1] < nums[p]) and (nums[p+1] <= nums[p])):
    #             break
            
    #         elif (( nums[p-1] > nums[p]) and (nums[p] < nums[p+1])):
    #             p -=1

    #         elif ((nums[p-1] < nums[p]) and (nums[p] > nums[p+1])):
    #             p +=1
                
    #     print(p)
        
    #     # Find the relevant part
        
    #     if target > nums[p]:
    #         l,r = 0,p
    #     if target <= nums[p]:
    #         l,r = p+1,n-1
            
    #     print(l,r)
        
    #     # Binary search on the relvant part
    #     n_relevant = len(nums[l:])
    #     while(l < r):
            
    #         mid = (l+r)//2
    #         print(nums[mid])
    #         if (target > nums[mid]):
    #             l = mid+1
    #         elif (target < nums[mid]):
    #             r = mid
    #         else:
    #             return mid
    #         print(l,r)
    #     return -1

    ### Approach 2 ####

    
    def search(self, nums: List[int], target: int) -> int:

        # Find the idx of the smallest number
        n = len(nums)
        lo, hi = 0, n-1

        while(lo < hi):
            mid = (lo + hi)//2
            if nums[mid] > nums[hi]:
                lo = mid+1
            else:
                hi = mid

        
        # Binary search accounting the rotation
        rot = lo
        lo, hi = 0,n-1

        while(lo <= hi):
            mid = (lo + hi)//2
            real_mid = (mid + rot)%n

            if nums[real_mid] == target:
                return real_mid
            if nums[real_mid] < target:
                lo  = mid+1
            else:
                hi = mid-1

        return -1

s = Solution()
print(s.search([4,5,6,7,0,1,2], 2))
