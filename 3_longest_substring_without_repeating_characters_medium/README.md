# 問題へのリンク

[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

# 言語
Python

# 問題の概要
文字列 `s` が与えられたとき、重複しない文字からなる最長の部分文字列(substring)の長さを求める問題。

# 自分の解法

文字列から文字`char`を1文字ずつ取り出していく。文字`char`を走査しているとき、そこから前にたどって最長の部分文字列（で文字が重複していないもの）を管理しながら走査していく。

- 各文字に対して、それが出現した最後のインデックスを記録するための辞書 `char_to_last_index` を用意してウィンドウ制御を行う。


- 時間計算量：`O(n)`
- 空間計算量：`O(1)`

## step2
- 変数名を変更：`substring_start_index` → `window_start_index`
- コメントを追加


# 別解・模範解答
ウィンドウ制御にsetを用いる方法もある。

https://wiki.python.org/moin/TimeComplexity より、setの要素の追加・削除は平均して`O(1)`であるため、以下のように書くことができる。

```python
while char in window_chars:
    window_chars.remove(s[left_index])  # O(1)
    left_index += 1
```


- 時間計算量：`O(n)`
- 空間計算量：`O(1)`

# 次に解く問題の予告
