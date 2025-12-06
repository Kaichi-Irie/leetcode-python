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

# tests
linked_list = DoubleLinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.appendleft(-1)
linked_list.appendleft(-2)
linked_list.pop()
linked_list.popleft()

print(linked_list.to_list()) # [-1, 1, 2]

# %%
