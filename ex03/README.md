# 第３回
## 迷路(ex03/maze.py)
### 追加機能
* スタート、ゴールの表示
* ゴールした時の歓喜メッセージ
* 通ったところにバツ印、
* 壁に行こうとするとゲームオーバー
* 通ったところのバツ印に入ってもゲームオーバー
* ゴールまでの時間を計測して、ゴール時に表示
### プログラム内の解説
* ゴールした時に表示するのはショウインフォ、そして講義で取り扱ったtmrを使用して時間計測
* dame()関数の中ではイフ文を使用して移動先が壁、もしくは通ってきた道だった場合にメッセージを出しプログラムを抜けるようにしている
* 通った時にバツ印を出すのはアップやダウンなどキーを押して移動したときに前の場所に画像を記している。
### 実装したかったもの
* もう一つrandomに移動して当たったらゲームオーバーになる敵キャラ