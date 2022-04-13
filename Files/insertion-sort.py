
def insertionSort(nums):

    for i in range(1, len(nums)):

        key = nums[i]
        j = i - 1
        
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key
    print(nums)
    return nums


if __name__ == "__main__":
    nums = [5, 2, 4, 6, 1, 3]
    insertionSort(nums)
