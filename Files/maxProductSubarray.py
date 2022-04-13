"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.
"""
import math
class Solution:
    def maxProduct(self, nums):
        if len(nums) == 1:
            return nums[0]

        ret, cur_pro, min_pro = nums[0],1, math.inf

        for num in nums:
            if cur_pro < min_pro:
                min_pro = cur_pro
                cur_pro = 1
                
            cur_pro *= num
            if cur_pro >= ret:
                ret = cur_pro
            
            print(f"Num: {num}\nCur_pro: {cur_pro}\nRet: {ret}\nMin_pro: {min_pro}")
        return ret

    def maxProduct_v2(self, nums):
        ret = nums[0]
        n = len(nums)

        for i in range(n):
            m = nums[i]

            for j in range(i+1, n):
                ret = max(ret, m)
                m *= nums[j]
            ret = max(ret, m)

        return ret

    def maxProduct_v3(self, nums):
        cur_max, cur_min, maxTotal = nums[0],nums[0],nums[0]
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0]

        for i in range(1,n):
            if nums[i] >= 0:
               cur_max = max(cur_max*nums[i],nums[i])
               cur_min = min(cur_min*nums[i],nums[i])
            else:
                temp = cur_max
                cur_max = max(cur_min*nums[i],nums[i])
                cur_min = min(temp * nums[i],nums[i])

            if maxTotal < cur_max:
                maxTotal = cur_max

        return maxTotal

soln = Solution()

print(soln.maxProduct_v3([-3,-1,-1]))
print(soln.maxProduct_v3([2,3,-2,4]))
print(soln.maxProduct_v3([-1,0]))
print(soln.maxProduct_v3([-2,0,-1]))