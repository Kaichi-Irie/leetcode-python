# 問題へのリンク

[Implement Trie (Prefix Tree) - LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/description/)

# 言語
Python

# 問題の概要
prefix tree（トライ木）を実装する問題。
3つのメソッドを実装する。
- `insert(word: str)`: 単語を挿入する。
- `search(prefix: str)`: 単語が存在するかを確認する。
- `startsWith(prefix: str)`: 単語が指定の接頭辞で始まるかを確認する。

# 自分の解法

`Trie`クラスには`char: str`と`children: dict[str, Trie]`というフィールドを持たせる。また、`is_final_char: bool`を持たせることで、単語の終端を示す。これにより、`apple`と`app`などの単語を区別できる。

走査は、`children`を辿っていく。再帰関数を使うことで、単語の各文字を順に確認していく。こうして`word`や`prefix`の最後の文字まで到達できれば、単語や接頭辞が存在することが確認できる。

`Trie`クラス自体が保持するデータは、各入力文字列の長さを`n_1, n_2, ...`とすると、最悪ケースでは`O(n_1+n_2+...)`の空間を使用する。（重複が多ければ、より少なくなる。）

各メソッドについて、`prefix`や`word`の長さを`n`とすると、以下のような時間計算量と空間計算量になる。

- 時間計算量：`O(n)`
- 空間計算量：`O(n)`
    - 再帰関数による実装のせいで各メソッドの呼び出しのたびにサイズ`n`のスタックを使用する。

## step2
- `char`フィールドを削除
    - 子ノードのキーとして文字を使用するため、`char`フィールドは不要。
- `startsWith`と`search`の実装で大きく重複していた処理を`_find_node_with`メソッドに切り出す。
    - `prefix:str`を引数に取り、`Trie`のノードを返す。
    - `prefix`の文字列が存在しない場合は`None`を返す。
- `search`メソッドは、`_find_node_with`を使って、単語の終端であるかを確認する。
- `startsWith`メソッドは、`_find_node_with`を使って、接頭辞が存在するかを確認する。
- `children = defaultdict(Trie)`を使って、`children`の初期化やキーの存在確認を簡潔にする。

- `head`, `tail`の変数名を`first_char`, `trailing_chars`に変更。


## step3
- v1. 16minかかってしまったのでやり直し

# 別解・模範解答
再帰関数を使わずに、`children`を辿るループで実装する。
- 時間計算量：`O(n)`
- 空間計算量：`O(1)`
    - 再帰関数を使わずに、`children`を辿るループで実装する。
- `TrieNode`クラスを作成し、`Trie`のノードを表現する。
    - `char: str`, `children: dict[str, TrieNode]`, `is_final_char: bool`のフィールドを持つ。
# 次に解く問題の予告
- [Subsets - LeetCode](https://leetcode.com/problems/subsets/)
- [Is Subsequence - LeetCode](https://leetcode.com/problems/is-subsequence/description/)
