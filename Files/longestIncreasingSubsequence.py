"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements 
without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

"""

class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)

        lis = [1]*n 

        for i in range(1,n):
            for j in range(0,i):
                if nums[i] > nums[j] and lis[i] < lis[j]+1:
                    lis[i] = lis[j]+1

        return max(lis)


soln = Solution()

nums = [10,9,2,5,3,7,101,18]

print(soln.lengthOfLIS(nums))