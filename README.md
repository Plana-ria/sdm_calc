# sdm_calc

## 使い方
`webserver.rb`にポート番号を設定する。

以下のコマンドで、開発サーバを立てる。

```
ruby webserver.rb
```

`localhost:port_num` にアクセスして、動作を確認したいcgiファイルを開く。

## `calc.cgi`の改良点について
- 入力した計算式を出力する機能を実装
- `%`演算子を実装
- `**`演算子を実装
- 演算子のみ、演算子で終わる式、演算子が連続する式などのエラー処理を改良
- 式内の空白の削除機能を実装