#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key --> value
        self.recently_used_keys = deque([])
        self.age = 0

    def get(self, key: int) -> int:
        # if key is not found, return -1
        if key not in self.cache:
            return -1
        value, _ = self.cache[key]
        self.cache[key] = (value, self.age)
        self.recently_used_keys.append((key, self.age))
        self.age += 1
        return value

    def put(self, key: int, value: int) -> None:
        if len(self.cache) < self.capacity or key in self.cache:
            self.cache[key] = (value, self.age)
            self.recently_used_keys.append((key, self.age))
            self.age += 1
        old_key, age = self.recently_used_keys.popleft()
        while age != self.cache[old_key][1]:
            old_key, age = self.recently_used_keys.popleft()
        self.cache.pop(old_key)
        # set the key as most recently used
        self.cache[key] = (value, self.age)
        self.recently_used_keys.append((key, self.age))
        self.age += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
