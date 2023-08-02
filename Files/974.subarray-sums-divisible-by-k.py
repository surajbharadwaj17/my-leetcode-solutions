#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ret = 0
        pre = 0
        count = [1] + [0] * k 

        for num in nums:
            pre = (pre + num) % k
            ret += count[pre]
            count[pre] += 1

        return ret 
        
# @lc code=end

