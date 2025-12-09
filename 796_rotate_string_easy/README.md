# 問題へのリンク
[796. Rotate String](https://leetcode.com/problems/rotate-string/)

# 言語
Python


# 自分の解法
全ての回転パターンを試す方法。枝刈りしたとしても、時間計算量は`O(n^2)`となる。


## step1

```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def is_same(string1: str, string2: str, offset: int) -> bool:
            for i in range(len(string1)):
                    if string1[i] != string2[(i+offset)%len(string2)]:
                        return False
            return True

        if len(s) != len(goal):
            return False
        if not s:
            return True
        matched_indices = [i for i in range(len(goal)) if goal[i]==s[0]]
        while matched_indices:
            offset = matched_indices.pop()
            if is_same(s, goal, offset):
                return True
        return False
```

- 時間計算量：`O(n^2)`
- 空間計算量：`O(1)`

## step2


## step3

## step4 (FB)



# 別解・模範解答
## 文字列の連結と部分文字列探索を利用する方法
文字列`s`を2回連結した文字列`s+s`を作成し、その中に`goal`が部分文字列として含まれているかを確認する方法。

- `str`に対して`in`演算子を使用することで、部分文字列の存在を`O(len(s))`で効率的にチェックできる。
    - `find`メソッドを使用すると、部分文字列の開始インデックスを取得できる。見つからなければ`-1`を返す。
    - これは、内部的にはKMPアルゴリズムやZアルゴリズムなどの効率的な文字列検索アルゴリズムを使用している。が、これらのアルゴリズムを手動で実装する必要は（コーディング面接の範囲では）なさそう

- 代わりに、Rabin-Karpアルゴリズムなどのハッシュベースの文字列検索アルゴリズムを実装することもできる。
    - Rabin-Karpアルゴリズムは、部分文字列のハッシュ値を計算し、効率的に検索を行う方法。
    - ローリングハッシュを使用するのが一般的。これは、ハッシュ値を差分的に高速（`O(1)`）に更新できる方法。


```python
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if not s:
            return True

        doubled_s = s+s
        return goal in doubled_s
```

- 時間計算量：`O(n)`
- 空間計算量：`O(n)`

自前でRabin-Karpアルゴリズムを実装する場合：
- Python標準の`hash`関数はプロセスごとに変わったりするので、文字に対するハッシュ関数は`ord(char)`などを使うのが良いかも
- `mod`は大きめの素数を使うのが一般的
- `base`も適当な素数を使うのが一般的

```python
def rolling_hash(string:str, base:int, mod:int)->int:
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
```

# 想定されるフォローアップ質問

## CS 基礎

## システム設計

## その他

# 次に解く問題の予告
