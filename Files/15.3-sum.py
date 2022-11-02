#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        n = len(nums)

        for i in range(n-2):
            if i>0 and nums[i] == nums[i-1]: continue  # skips duplicates

            left, right = i+1, n-1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]

                if cur_sum < 0: # We need a bigger number, hence move left
                    left += 1
                elif cur_sum > 0: # We need a smaller number, hence move right
                    right -= 1
                else:
                    ret.append([nums[left], nums[i], nums[right]])  # Found the triplet! Record it and move both pointers
                    
                    while left<right and nums[left] == nums[left+1]: # Skip duplicates
                        left += 1

                    while left<right and nums[right] == nums[right-1]: # Skip duplicates
                        right -= 1

                    left += 1
                    right -= 1

        return ret
        
# @lc code=end

