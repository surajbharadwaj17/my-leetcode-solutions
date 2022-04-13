"""
Find the duplicate items in a given array

logic: Flip the sign if an item is positive. Item with negative sign is a repition
"""

def findDuplicates(nums):
    duplicates = []
    for num in nums: 
        if nums[abs(num)-1] >= 0:
            nums[abs(num)-1] = - nums[abs(num)-1]
        else:
            duplicates.append(abs(num))
    return duplicates

print(findDuplicates([4,3,2,7,8,2,3,1]))

