"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


    

def threeSum(nums):
    ret = []
    nums = sorted(nums)
    for i in range(len(nums)-2):
        # skip the same numbers
        if i > 0 and nums[i] == nums[i-1]:
            continue

        L,R = i+1, len(nums)-1

        while(L<R):
            cur_sum = nums[i]+nums[L]+nums[R]

            if cur_sum < 0:
                L += 1
            elif cur_sum > 0:
                R -= 1
            else:
                ret.append(sorted([nums[i],nums[L], nums[R]]))

                # Move the 2 pointers to skip the same numbers
                while(L < R and nums[L] == nums[L+1]):
                    L += 1

                while(L < R and nums[L] == nums[L+1]):
                    R -= 1

                L += 1
                R -= 1

    return ret
nums = [-1,0,1,2,-1,4]


print(threeSum(nums))
