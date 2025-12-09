#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start

def rolling_hash(string:str,base:int, mod:int)->int:
    hash_val = 0
    for char in string:
        hash_val = (base*hash_val + ord(char))%mod
    return hash_val

def contains_pattern(text:str, pattern: str, base=101, mod=10**9+7)->bool:
    if len(pattern) > len(text):
        return False
    pattern_hash = rolling_hash(pattern,base,mod)
    substring_hash = rolling_hash(text[:len(pattern)],base,mod)
    # substring = string[i:i+m] i = 0, ..., n-m
    for i in range(len(text)-len(pattern)+1):
        # substring_hash = rolling_hash(string[i:i+m])
        if pattern_hash == substring_hash and pattern == text[i:i+len(pattern)]:
            return True
        if i+len(pattern) < len(text):
            left = ord(text[i])
            right = ord(text[i+len(pattern)])
            substring_hash = (substring_hash-left*pow(base,len(pattern)-1,mod))%mod
            substring_hash = (base*substring_hash +right)%mod
    return False


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if not s:
            return True
        doubled_s = s+s
        return contains_pattern(doubled_s, goal)

# @lc code=end
