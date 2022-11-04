#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        import collections
        # If s and t are not of the same length, they are not anagrams.
        # Count the characters in one string. 
        # For each occurrence of the char in other string, decrement the count in s
        # At the end, if both strings are anagrams, all the counts will be zero

        count = collections.Counter(s)
        for char in t:
            if char not in t:
                return False
            else:
                count[char] -= 1

        for key in count:
            if count[key] != 0:
                return False
        return True

        
# @lc code=end

