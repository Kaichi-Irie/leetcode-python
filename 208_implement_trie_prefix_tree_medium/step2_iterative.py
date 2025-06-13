#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#


# %%
# @lc code=start
class Trie:
    def __init__(self):
        self.char = ""
        self.children: dict[str, Trie] = {}
        self.is_final_char = False

    def insert(self, word: str) -> None:
        if not word:
            return

        node: Trie = self
        for char in word:
            if char not in node.children:
                node.children[char] = Trie()
                node.children[char].char = char
            node = node.children[char]
        node.is_final_char = True
        return

    def search(self, word: str) -> bool:
        final_node = self._find_node_with(word)
        if final_node is None:
            return False
        elif not final_node.is_final_char:
            return False
        else:
            return True

    def startsWith(self, prefix: str) -> bool:
        final_node = self._find_node_with(prefix)
        return final_node is not None

    def _find_node_with(self, prefix: str) -> "Trie":
        if not prefix:
            return self

        node: Trie = self
        for i, char in enumerate(prefix):
            if not node:
                return None
            elif char not in node.children:
                return None
            node = node.children[char]
        return node


# %%

# %%
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
