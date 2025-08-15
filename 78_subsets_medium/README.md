# 問題へのリンク
[Subsets - LeetCode](https://leetcode.com/problems/subsets/description/)


# 言語
Python

# 問題の概要
与えられた整数のリストから、すべての部分集合を生成する問題。


# 自分の解法 bit演算を用いて解く
全ての部分集合は、`nums`の要素数を`n`としたとき、`2^n`通り存在する。各部分集合は、`0`から`2^n - 1`までの整数をビットマスクとして解釈することで生成できる。

- 時間計算量：`O(n * 2^n)`
- 空間計算量：`O(n * 2^n)`

## step2
- `_ith_binary_digit`関数を定義して、整数をビットマスクとして解釈する際に、`i`番目のビットが立っているかどうかを判定する処理を分離した。

# 別解1. backtracking
- backtrackingを用いて部分集合を生成する方法。再帰的に要素を選択するかどうかを決定し、部分集合を構築していく。`subset`リストはオブジェクトの操作で更新され、最後に`all_subsets`に追加するときにコピーされる。そのため、思わぬところに影響が出ないように更新の順序に注意が必要。
    - なお、Pythonの値渡し、参照渡し、参照の値渡しについては、[こちら](https://note.com/crefil/n/n7a0d2dec929b)を参照。
        - 値渡し
            - 呼び出し先で再代入した場合
                - 呼び出し元に影響なし
            - 呼び出し先でオブジェクトの操作をした場合
                - 呼び出し元に影響なし
        - 参照渡し
            - 呼び出し先で再代入した場合
                - 呼び出し元変数の参照先も変わる
            - 呼び出し先でオブジェクトの操作をした場合
                - 呼び出し元変数が参照しているオブジェクトも変わる
        - 参照の値渡し
            - 呼び出し先で再代入した場合
                - 呼び出し元変数の参照先は変わらず、影響を受けなくなる
            - 呼び出し先でオブジェクトの操作をした場合
                - 呼び出し元変数が参照しているオブジェクトも変わる
- backtrackingはコードが簡潔だが、可読性が低くなることがあると感じた

- 時間計算量：`O(n * 2^n)`
- 空間計算量：`O(n * 2^n)`
[こちら](https://www.youtube.com/watch?v=3JWtSMlq0Sw)の動画を参考にした。

# 別解2. 再帰的な方法
- (backtrackingとは異なる方法で)再帰的に部分集合を生成する方法。
- `subsets(nums: list[int])`関数を用いて再帰を回す
- `subsets(nums[1:])`に`nums[0]`を含める場合と含めない場合の2通りを考えて、全ての部分集合を生成する。
- 時間計算量：`O(n * 2^n)`
- 空間計算量：`O(n * 2^n)`

# 次に解く問題の予告
- [Evaluate Division - LeetCode](https://leetcode.com/problems/evaluate-division/description/)
- [Subsets II - LeetCode](https://leetcode.com/problems/subsets-ii/description/)
