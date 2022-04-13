"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

class Solution:
    def isAnagram(self, s,t):
        import collections 

        if len(s) != len(t):
            return False
        
        count1, count2 = collections.Counter(s), collections.Counter(t)

        for key in count1.keys():
            if (key not in count2) or (count1[key] != count2[key]):
                return False

        return True


soln = Solution()
s = 'a'
