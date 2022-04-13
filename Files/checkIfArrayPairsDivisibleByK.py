"""
Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair
 is divisible by k.

Return true If you can find a way to do that or false otherwise.
"""


class Solution:
    def canArrange(self, nums, k):
        hmap = {}
        pairs = []
        for num in nums:
            if num not in hmap:
                hmap[num] = True
                
        for num in nums:
            if k - num in hmap:
                pairs.append((num, k-num))
        print(hmap)
        print(pairs)
        if len(pairs) == len(nums)//2:
            return True
        else:
            return False


soln = Solution()
nums = [1,2,3,4,5,10,6,7,8,9]
k = 5
print(soln.canArrange(nums,k))