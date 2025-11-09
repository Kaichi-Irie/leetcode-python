#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_groups = defaultdict(list)
        for word in strs:
            canonical_key = self._generate_anagram_key(word)
            anagram_groups[canonical_key].append(word)
        return list(anagram_groups.values())

    def _generate_anagram_key(self, word: str) -> str:
        return "".join(sorted(word))


# @lc code=end
