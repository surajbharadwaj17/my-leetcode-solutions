#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mx_len, start = 0,0
        used = {}

        for i, char in enumerate(s):
            # If we encounter an already seen char and the last occurrence of that char 
            # is actually smaller than the starting index, we found a repeating character. 
            # so change the starting point
            if char in used and start <= used[char]: 
                start = used[char] + 1
            else:
                # If it is a non-repeating character, update the max length
                mx_len = max(mx_len, i-start+1)
            used[char] = i
            
        return mx_len
        
# @lc code=end

