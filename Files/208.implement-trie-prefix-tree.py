#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
from collections import defaultdict


class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.children[char]

        cur.is_word = True

    def search(self, word: str) -> bool:
        
        cur = self.root

        for letter in word:
            cur = cur.children.get(letter)

            if not cur:
                return False

        return cur.is_word


    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for letter in prefix:

            cur = cur.children.get(letter)
            if not cur:
                return False

        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

