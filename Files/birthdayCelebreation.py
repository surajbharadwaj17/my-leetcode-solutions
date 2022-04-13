"""
In the hostel, there are birthday celebrations every month. Given N number of days which are representing the birthday, find the number of days where there are an odd number of birthday celebrations.
Input:
The first line of the input consists of an integer days_size representing the number of birthdays celebrations (N).
The second line of the input consists of N space-separated integers days representing the birthdays' celebrations in a month.
Output:
Print an integer representing the number of days where there is an odd number of birthday celebrations.
Example:
Input:
5
4 8 2 8 9

Output:
3

Explanation: 4, 2 and 9 occur only once (1 is odd). So, the answer is 3.
"""
import collections

def birthdayCelebration(n, nums):
    count = collections.Counter(nums)
    bday_cnt = 0
    for k in count.keys():
        if count[k] % 2 != 0:
            bday_cnt += 1
    return bday_cnt


n = int(input())
nums = list(input())

print(birthdayCelebration(n,nums))