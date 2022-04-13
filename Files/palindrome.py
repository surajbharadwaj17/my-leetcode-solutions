"""
Check whether the given string is a palindrome or not
"""

def palindrome(string):
    """
    #python one-liner
    if string == string[::-1]:
        return True
    else:
        return False
    """
    start = 0
    last = len(string)-1
    while(start < last):
        if string[start] != string[last]:
            return False
        start +=1
        last -=1
    return True

print(palindrome('sooraj'))