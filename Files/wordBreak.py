"""
Given a string s and a dictionary of strings wordDict, return true 
if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

"""

class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:

                if ( word == s[i-len(word)+1 : i+1] ) and (dp[i-len(word)] or i-len(word)==-1):
                    dp[i] = True

        return dp[-1]



soln = Solution()
s = 'leetcode'
wordDict = ["leet", 'code']
print(soln.wordBreak(s,wordDict))


"""

The idea is the following:

d is an array that contains booleans

d[i] is True if there is a word in the dictionary that ends at ith index of s AND d is also True at the beginning of the word

Example:

s = "leetcode"

words = ["leet", "code"]

d[3] is True because there is "leet" in the dictionary that ends at 3rd index of "leetcode"

d[7] is True because there is "code" in the dictionary that ends at the 7th index of "leetcode" AND d[3] is True

The result is the last index of d.

"""