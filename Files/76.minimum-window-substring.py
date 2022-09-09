#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        # Keep the target length to be achieved
        tlen = len(t)
        # Return string
        mwin = ""
        # Keep the count of target chars
        count = collections.Counter(t)
        # We fix the end pointer and move the window by sliding the start pointer
        start, end = 0,0

        for end in range(len(s)):
            # If current char is found in count, decrement the target len
            if count[s[end]] > 0:
                tlen -= 1
            # Decrement the count of current char in dict
            count[s[end]] -= 1

            # If we have found all the target chars, check for min length
            while(tlen == 0):
                wlen = end - start + 1
                # If smaller window is found, update the min window
                if not mwin or len(mwin) > wlen:
                    mwin = s[start:end+1]
                # Incerement the count of current char
                count[s[start]] += 1

                # Break out of the loop if we have found all target letters 
                if count[s[start]] > 0:
                    tlen += 1

                # Move the window by incrementing start
                start += 1

        return mwin
        
            
                     
# @lc code=end

