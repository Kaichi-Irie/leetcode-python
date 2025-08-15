#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#


# %%
# @lc code=start
# TrieNode has char:str, children: dict[str, TrieNode], and is_final_char
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = defaultdict(TrieNode)
        self.word_ends_here = False


# Trie has root TrieNode
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node: TrieNode = self.root
        for char in word:
            node = node.children[char]
        node.word_ends_here = True

    def search(self, word: str) -> bool:
        node: TrieNode = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word_ends_here

    def startsWith(self, prefix: str) -> bool:
        node: TrieNode = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# %%

# %%
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
