#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums = sorted(nums)
        n = len(nums)

        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, n-1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum < 0:
                    left += 1
                elif cur_sum > 0:
                    right -= 1
                else:
                    ret.append([nums[i], nums[left], nums[right]])

                    while(left< right and nums[left]==nums[left+1]):
                        left += 1
                    
                    while(left<right and nums[right]==nums[right-1]):
                        right -= 1

                    left += 1
                    right -= 1

        return ret
        
# @lc code=end

