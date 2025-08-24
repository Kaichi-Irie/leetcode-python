#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#


# @lc code=start
from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.is_final_char = False

    # TC: O(len(word))
    # SC: O(len(word))
    def insert(self, word: str) -> None:
        if not word:
            self.is_final_char = True
            return
        first_char, trailing_chars = word[0], word[1:]
        child_node: Trie = self.children[first_char]
        child_node.insert(trailing_chars)

    def search(self, word: str) -> bool:
        final_node: Trie | None = self._find_prefix_node(word)
        # word is not found
        if final_node is None:
            return False
        # no word end at the final node
        elif not final_node.is_final_char:
            return False
        # word end at the final node
        else:
            return True

    def startsWith(self, prefix: str) -> bool:
        final_node: Trie | None = self._find_prefix_node(prefix)
        return final_node is not None

    # TC: O(len(prefix))
    # SC: O(len(prefix))
    from typing import Optional

    def _find_prefix_node(self, prefix: str) -> Optional["Trie"]:
        if not prefix:
            return self
        first_char, trailing_chars = prefix[0], prefix[1:]
        if first_char not in self.children:
            return None
        child_node: Trie = self.children[first_char]
        return child_node._find_prefix_node(trailing_chars)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
