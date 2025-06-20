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
        anagram_groups: dict[str, list[str]] = defaultdict(list)

        for word in words:
            canonical_key: str = self.generate_anagram_key(word)
            anagram_groups[canonical_key].append(word)
        return list(anagram_groups.values())

    # canonical key of a word is generated by sorting each characters in it
    def generate_anagram_key(word: str) -> str:
        return "".join(sorted(word))


# @lc code=end
