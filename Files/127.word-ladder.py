#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        length = 1
        
        # Edge cases
        if len(beginWord) != len(endWord) : return 0
        if endWord not in words: return 0

        q = collections.deque([[beginWord, length]])
        # BFS
        while(q):
            word, length = q.popleft()
            # Base case
            if word == endWord:
                return length

            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz': # Replace i-th character and search for each possible result
                    next_word = word[:i] + char + word[i+1:]
                    if next_word in words:      # Append to the queue if new_word is found in word list
                        words.remove(next_word) # Remove to avoid returning to the same found after replacing.
                        q.append([next_word, length+1]) # Add to the queue

        return 0

        

        
# @lc code=end

