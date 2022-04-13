"""
You are given a string s and an integer k.
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing 
the above operations.


"""

class Solution:
    def characterReplacement(self, s, k):
        import collections
        count = collections.defaultdict(int)
        max_len, max_cnt = 0,0

        for i in range(len(s)):

            count[s[i]] += 1
            max_cnt = max(max_cnt, count[s[i]])

            if max_len < max_cnt+k:
                max_len += 1
            else:
                count[s[i - max_len]] -= 1

        return max_len

soln = Solution()
s = 'AABABBA'
k = 1

print(soln.characterReplacement(s,k))