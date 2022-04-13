"""
reverse the given integer
"""
def reverseInteger(num):
    rev_num= 0
    while(num > 0):
        rem = num %10
        num = num//10
        rev_num = rev_num * 10 + rem
    return rev_num

print(reverseInteger(12340))