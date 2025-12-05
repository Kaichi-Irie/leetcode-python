#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key --> NodeList
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node

    def add_to_front(self, node):
        old_front = self.head.next
        old_front.prev = node
        node.next = old_front
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        # If key is not found, return -1
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # when key exists
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add_to_front(node)
            return

        node = ListNode(key, value)
        self.cache[key] = node
        self.add_to_front(node)
        # if cache is full, remove the least recently used node
        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self.cache.pop(lru_node.key)
            self.remove(lru_node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
