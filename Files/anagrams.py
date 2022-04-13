"""
Check if the given 2 strings are anagrams are not (same letters)
"""
def isAnagram(str1,str2):
    if len(str1) != len(str2):
        return False
    
    if sorted(str1) == sorted(str2):
        return True
    else :
        return False

print(isAnagram('flusteg','restful'))