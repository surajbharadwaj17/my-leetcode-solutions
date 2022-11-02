#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #import collections

        #count = collections.Counter(nums)
        count = {}
        n = len(nums)
        for n in nums:
            if n not in count: count[n] = 1
            else:
                count[n] += 1
                if count[n] >= n//2:
                    return n
    
        
# @lc code=end

