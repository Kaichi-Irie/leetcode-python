# 問題へのリンク
[8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

# 言語
Python


# 自分の解法
dislikesが多いのは、LeetCodeらしからぬ細かい仕様が多いから？
## step1

```python
class Solution:
    CHAR_TO_DIGIT = {str(i): i for i in range(10)}

    def myAtoi(self, s: str) -> int:
        SPACE = " "
        PLUS = "+"
        MINUS = "-"
        MIN = -(2**31)
        MAX = 2**31 - 1
        if not s:
            return 0
        num = 0
        # remove leading whitespaces
        i = 0
        while i < len(s) and s[i] == SPACE:
            i += 1
        s = s[i:]
        if not s:
            return 0
        # process sign
        is_negative = False
        if s[0] == PLUS:
            s = s[1:]
        elif s[0] == MINUS:
            s = s[1:]
            is_negative = True
        if not s:
            return 0
        # conversion
        digits: list[int] = []
        for char in s:
            if char not in self.CHAR_TO_DIGIT:
                break
            digit = self.CHAR_TO_DIGIT[char]
            digits.append(digit)
        digits.reverse()
        for i, digit in enumerate(digits):
            num += digit * pow(10, i)
        num = -num if is_negative else num
        # rounding
        num = min(num, MAX)
        num = max(num, MIN)

        return num
```
- leading whitespace を取り除く箇所で何度かミスってしまった
    - まず`s.replace(" ", "")`で全ての空白を取り除いてしまっていた
    - 次に前から空白を取り除く処理を実装したが、何度かバグを踏んだ
    - `while i < len(s) and ...`と先にandしておくと、`i`が`len(s)`に達したときに`s[i]`でIndexErrorになる問題を防げる

- 時間計算量：`O(n)`
- 空間計算量：`O(n)`

## step2

```python
class Solution:
    CHAR_TO_DIGIT = {str(i): i for i in range(10)}
    def myAtoi(self, s: str) -> int:
        SPACE = " "
        PLUS = "+"
        MINUS = "-"
        MIN_INT = -(2**31)
        MAX_INT = 2**31 - 1
        if not s:
            return 0
        num = 0

        # remove leading whitespaces
        i = 0
        while i < len(s) and s[i] == SPACE:
            i += 1
        # process sign
        sign = 1
        if i < len(s) and s[i] == PLUS:
            i += 1
        elif i < len(s) and s[i] == MINUS:
            i += 1
            sign = -1
        # conversion
        while i < len(s) and s[i] in self.CHAR_TO_DIGIT:
            digit = self.CHAR_TO_DIGIT[s[i]]
            num = num * 10 + digit
            i += 1
        num = sign * num
        # rounding
        num = min(num, MAX_INT)
        num = max(num, MIN_INT)

        return num
```


- 文字列のスライスを使わないようにした。これにより、`O(n)`の時間計算量と`O(1)`の空間計算量で実装できる
- `is_negative`を`sign`に変更した
    - `sign`を`1`か`-1`にしておくと、最後に`num=sign*num`とするだけで済む


最後の変換部分のロジックを
```python
digits.reverse()
for i, digit in enumerate(digits):
    num += digit * pow(10, i)
```
から
```python
for digit in digits:
    num = num * 10 + digit
```
と書き換えた
- `digits`を逆順にする必要がなくなった
- `pow`を使わなくなった
- `num=0`から始めて、`num=num*10+digit`を繰り返すことで、上の位の桁から順に処理できる

- > `ord(s[pos]) - ord('0')`の代わりに`int(s[pos])`とかも選択肢としてあり。とはいえこれをするんだったら`int(s[index:])`みたいにやっていいじゃんという気持ちにもなるので、この問題的にはint使わない方が空気が読めてそう。
- `ord`を使う方法もある
(ref: https://github.com/hayashi-ay/leetcode/pull/69/files)
- `is_digit`メソッドについて調べる

## step3

## step4 (FB)



# 別解・模範解答

- 時間計算量：`O(n)`
- 空間計算量：`O(n)`

# 想定されるフォローアップ質問

## CS 基礎

## システム設計

## その他

# 次に解く問題の予告
- Permutations
