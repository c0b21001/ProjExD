# 第2回
## 電卓(ex02/test.py)
### 追加機能
* +,-,*,**,/などの演算子の追加
* %を押したときに(1)であれば(1.0%)
* ACを押したときに全部消える
* +/-を押したときに符号が変わる
* delを押した時に一文字消える
### プログラム無いの解説
* click_AC関数では
entry.delete(0,tk.END)ですべて消える
* click_hanten関数では押したときに一度数値をリスト化して、最初に-を付け足す。もし既についていたらリストの一文字目を取り除く。1
* click_percent関数では.insertを使用してリストの３番目に.を入力する。
もし.countにより.が入っているとカウントされたら指定して削除される。
* click_del関数では指定の要素にclick_delを入れentry.delete(len(s)-1,tk.END)によって一文字戻す
### 実装したかったもの
* 問題が表示されてその答えを入力するようなクイズ的なプログラム