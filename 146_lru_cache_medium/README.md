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

- 各操作について時間計算量：ならしで`O(1)`
- 空間計算量：`O(n)`


テストケース
```python
```


## step2

```python

```

ついでに自分で`DoubleLinkedList`を実装してみた。
- `head`, `tail`のダミーノードを用いることで、境界条件を気にせずに済む。
- `_insert_between`でノードの挿入をまとめて行うと楽。
- `deque`のメソッド名に合わせ、`append`, `appendleft`, `pop`, `popleft`を実装した。
- ミニマルな実装では、`__len__`や`__iter__`、`to_list`は不要だが、デバッグやテストに便利なので実装しておいた。

```python
class Node:
	def __init__(self, val=0):
		self.val = val
		self.next: Node|None = None
		self.prev: Node|None = None

class DoubleLinkedList:
	def __init__(self):
		self.head = Node()
		self.tail = Node()
		self.head.next = self.tail
		self.tail.prev = self.head
		self.size = 0

	def _insert_between(self, node: Node, prev:Node, next_:Node):
		prev.next = node
		node.prev = prev
		next_.prev = node
		node.next = next_
		self.size += 1


	def remove(self, node:Node):
		if node is self.head or node is self.tail:
			raise ValueError
		next_node = node.next
		prev_node = node.prev

		next_node.prev = prev_node
		prev_node.next = next_node
		self.size -= 1

	def pop(self) -> Node|None:
		if self.size == 0:
			return None
		node = self.tail.prev
		self.remove(node)
		return node

	def popleft(self) -> Node|None:
		if self.size == 0:
			return None
		node = self.head.next
		self.remove(node)
		return node

	def append(self, val: int):
		node = Node(val)
		self._insert_between(node, self.tail.prev, self.tail)

	def appendleft(self, val: int):
		node = Node(val)
		self._insert_between(node, self.head, self.head.next)

	def __len__(self) -> int:
		return self.size

	def __iter__(self):
		node = self.head.next
		while node is not self.tail:
			yield node.val
			node = node.next

	def to_list(self):
		return [val for val in self]
```

## step3

## step4 (FB)



# 別解・模範解答

双方向連結リストのノードへのポインタをハッシュマップで管理する方法。
これなら、削除や挿入をO(1)で行える。
put、getのどちらでも、キャッシュの順番を更新する必要があることに注意。
`add_to_front`と`remove_node`を用いて、ノードの移動を行うと楽。
ダミーの`head`, `tail`ノードを用いると、境界条件を気にせずに済む。

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

- 各操作について時間計算量：`O(1)`
- 空間計算量：`O(capacity)`

`collections.OrderedDict`を用いる方法もある。

```python
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache= OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

# 想定されるフォローアップ質問

## CS 基礎

## システム設計

## その他

# 次に解く問題の予告
