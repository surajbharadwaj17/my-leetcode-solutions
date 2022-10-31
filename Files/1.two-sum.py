#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Brute force - Using 2 loops -> O(N^2?)
        """for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                    """

        # Using a hash map
        hmap = {}

        for i in range(len(nums)):      # Looping thru' the input only once -> O(N)
            if target - nums[i] in hmap: # Constant lookup time for dict
                return [i, hmap[target-nums[i]]]
            else:
                hmap[nums[i]] = i

        return -1

        
# @lc code=end

