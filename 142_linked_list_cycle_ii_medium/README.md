# 問題へのリンク
[142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

# 言語
Python

# 問題の概要
与えられた連結リストがサイクルを持つ場合、そのサイクルの開始ノードを返す。サイクルがない場合は`None`を返す。

# 自分の解法

## step1

`visited`セットを用いて到達済みノードを記録する方法。


```python
class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        visited = set()
        node = head
        while node:
            if node in visited:
                return node
            visited.add(node)
            node = node.next
        return node
```

- 自作オブジェクトはhashableなので、setやdictのキーとして使用できる
    - デフォルトでは`__hash__`メソッドが`hash(id(self))`を返すため、オブジェクトのIDに基づいてハッシュ値が生成される
    - デフォルトでは`__eq__`メソッドは`id(self) == id(other)`を返すため、オブジェクトのIDに基づいて等価性が判断される
    - `__eq__`メソッドが定義されている場合、`__hash__`メソッドも**適切に**定義する必要がある
        - `a==b`が`True`の場合、`hash(a)`と`hash(b)`も等しくなる必要がある


- 時間計算量：`O(n)`
- 空間計算量：`O(n)`

## step2

## step3

`step3.py`
```python
class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        seen_nodes = set()
        node = head
        while node:
            if node in seen_nodes:
                return node
            seen_nodes.add(node)
            node = node.next
        return None
```

`step3_two_pointers.py`
やはりフロイドのアルゴリズムは読んでいてわかりにくいので、docstringを追加してみた。

```python
class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        """
        Detect if a cycle exists and if so, where the cycle starts.
        This uses Floyd's algorithm for efficient space complexity.
        """
        slow_pointer = head
        fast_pointer = head
        have_cycle = False
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if fast_pointer == slow_pointer:
                have_cycle = True
                break
        if not have_cycle:
            return None

        pointer1 = head
        pointer2 = fast_pointer

        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1
```


## step4 (FB)



# 別解・模範解答
フロイドのアルゴリズムを使用する方法。

```python
class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return None

        slow_pointer = head
        fast_pointer = head
        exists_cycle = False
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                exists_cycle = True
                break

        if not exists_cycle:
            return None

        slow_pointer = head
        while slow_pointer != fast_pointer:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next
        return slow_pointer
```

まずは、2つのポインタを用いてサイクルの存在を検出する。次に、サイクルの開始ノードを特定する。
1. 2つのポインタ（`slow`と`fast`）を用意し、`slow`は1ステップずつ、`fast`は2ステップずつ進める。
2. もし`slow`と`fast`が衝突した場合、サイクルが存在する。
3. サイクルの開始ノードを特定するために、`slow`をリストの先頭に戻し、`fast`はそのままの位置に置く。両方を1ステップずつ進めて次に衝突するノードがサイクルの開始ノードである。

- ループが`break`されず。正常に終了したかどうかを表す`for ... else`はEffective Pythonではバッドプラクティスとされているため、`exists_cycle`フラグを使用している。

- 時間計算量：`O(n)`
- 空間計算量：`O(1)`

# 次に解く問題の予告
- [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)
- [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)
