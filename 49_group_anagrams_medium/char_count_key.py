#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, words: list[str]) -> list[list[str]]:
        # manage anagrams as a hashmap whose key is "canonical key" and value is a list of anagrams
        anagram_groups: dict[tuple[str], list[str]] = defaultdict(list)

        for word in words:
            canonical_key = self.generate_anagram_key(word)
            anagram_groups[canonical_key].append(word)
        return list(anagram_groups.values())

    def generate_anagram_key(self, word: str) -> tuple[str]:
        char_count = [0] * 26
        for char in word:
            order = ord(char) - ord("a")
            char_count[order] += 1
        return tuple(char_count)


# @lc code=end
