# 問題へのリンク
[146. LRU Cache](https://leetcode.com/problems/lru-cache/)

# 言語
Python

# 自分の解法


## step1
dequeを用いて、キャッシュの順番を管理する方法。lazy deletionを用いることで、dequeの中身を直接削除しないようにする。
ならし計算量O(1)にはなるが、最悪計算量O(n)になる可能性がある。また、メモリも増えやすい。

```python
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
```

- 時間計算量：`O(n)`
- 空間計算量：`O(n)`

テストケース
```python
```


## step2

```python

```

## step3

## step4 (FB)



# 別解・模範解答

双方向連結リストのノードへのポインタをハッシュマップで管理する方法。
これなら、削除や挿入をO(1)で行える。
put、getのどちらでも、キャッシュの順番を更新する必要があることに注意。
`add_to_front`と`remove_node`を用いて、ノードの移動を行うと楽。

```python
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
```

- 時間計算量：`O(n)`
- 空間計算量：`O(n)`

テストケース
```python
```

# 想定されるフォローアップ質問

## CS 基礎

## システム設計

## その他

# 次に解く問題の予告
- Permutations
