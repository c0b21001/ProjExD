# 第7回
## KOUKATONKING(ex06/jump4.py)
### 追加機能
* CSVファイルを使用して、ファイル内の数値に応じて地面などを描画するようになっている。
* 画面の中で右1/5と左1/5をプレイヤーが行ける端を定義し、その端っこでさらに進もうとすると地面がスクロールするようになっている。
* 地面の間の穴に落ちて、画面の一番下につくと左端で復活。
* 右移動、左移動、ジャンプ（スペース）機能の追加。
* プレイヤーが壁に接触すると跳ね返る。（澤木）
* 背景画像を自動スクロール（森川）
### プログラム内の解説
* importを使用してpygameとCSVをインポートする
* 初期値の設定7~32行目
* あらかじめ数値を入力したCSVファイルを用意して、そのCSVファイルをwith openを使用して開く。35行目
* stageクラスではCSVファイルの数値に対応した地面などをtileとして場所を決め描画
* playerクラスでは自分が操作するキャラの画像、空中にいるなどの状態、そしてキーを押したときの動作を設定、その後当たり判定の設定、そしてジャンプした時に地面に落ちてくるような重力の設定。
* GAMEクラスでは穴に落ちた時の動作や画面の初期化、ステージの描画などと、プレイヤーが端に来た時のスクロールを実装
### 実装したかったもの
* スクロールが今現在横だけなので縦にスクロールできるようにしたい。
* ジャンプするときにジャンプキングを目指しているので溜めを作りたい。
* ステージの地面を可動式にしたい。（島田↓）
* ゴール地点の設定をしたい。
* スペースをおしっぱだと、リスポーンできないバグを修正したい。無限に縦スクロールしてしまう。
### 参加メンバー
* C0B21001　相澤瑞希
* C0B21077　澤木優一郎
* C0B21081　島田和音
* C0B21129　長谷川陸人
* C0B21151　森川蒼