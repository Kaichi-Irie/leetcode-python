#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#


# %%
# @lc code=start
class Trie:
    def __init__(self, root=""):
        self.root = root
        self.children: dict[str, Trie] = {}  # character -> Trie Tree
        self.is_terminal = False

    def insert(self, word: str) -> None:
        if not word:
            self.is_terminal = True
            return

        head, tail = word[0], word[1:]
        if head not in self.children:
            self.children[head] = Trie(root=head)
        child: Trie = self.children[head]
        child.insert(tail)

    def search(self, word: str) -> bool:
        if not word:
            return self.is_terminal
        head, tail = word[0], word[1:]
        if head not in self.children:
            return False
        else:
            child: Trie = self.children[head]
            return child.search(tail)

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return True
        head, tail = prefix[0], prefix[1:]
        if head not in self.children:
            return False
        child: Trie = self.children[head]
        return child.startsWith(tail)


# %%

# %%
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
