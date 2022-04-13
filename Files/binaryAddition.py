"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""

def getSum(a,b):
    """
    :type a: int
    :type b: int
    :rtype: int
    """
    if b == 0:
        return a
    else:
        return getSum(a^b, (a&b)<<1)

    return (a | b) - (a & b)


a, b = 2,3
print(getSum(a,b))