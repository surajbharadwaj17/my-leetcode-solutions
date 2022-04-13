"""
Problem statement:

Reverse a given array (arr) in O(N) without using additional memory
"""

def reverseArray(arr):
    first = 0
    last = len(arr) - 1

    while(first < last):
        temp = arr[last]
        arr[last] = arr[first]
        arr[first] = temp

        first +=1
        last -=1
    return arr

arr = [1,2,3,4,5]

print(reverseArray(arr))