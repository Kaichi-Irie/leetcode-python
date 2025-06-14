#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#


# @lc code=start
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        # hasmap: standardized key -> list of anagrams
        hashmap = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            hashmap[key].append(word)

        return [anagrams for anagrams in hashmap.values()]


# @lc code=end
