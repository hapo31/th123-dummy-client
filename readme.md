# これはなに
天則のクライアントに偽装して、接続を待ち受けているサーバーに接続リクエストパケットを送るスクリプトです。
# メモ
天則のクライアントは接続時に以下のような形式でパケットを送りつけるらしい。(ソースから抜粋)
```
0x00    0x01, # 固定 1byte
0x01    0x02, 0x00, 0x2a, 0x30, # 固定 4bytes
0x05    0x7f, 0x00, 0x00, 0x01, 0x00, 0x02, 0x00, 0x80, 0x69, 0x00, 0x69, 0x00, # バージョン情報 12bytes
0x11    0x02, 0x00, 0x2a, 0x30, # 固定 4bytes
0x15    0x7f, 0x00, 0x00, 0x01, 0x00, 0x02, 0x00, 0x80, 0x69, 0x00, 0x69, 0x00, # バージョン情報 12bytes
0x21    [送信回数情報4bytes]
```

で、バージョン情報はこれで固定ではないらしく、以下のようなパターンも観測している
```
0x7f, 0x00, 0x00, 0x01, 0x55, 0x55, 0x55, 0x55, 0x00, 0x00, 0x00, 0x00
```
クライアントを再起動するたびにこの2種類(暫定)が切り替わるらしい。(法則不明)

# 送信回数
以下のような法則で計算されるらしい。

```
def _get_sendcount(self, sendcount):
    if sendcount % 5 < 3:
        return 0
    if sendcount % 5 < 4:
        return #不明#

    return #不明#
```
この#不明#の部分は今のところ本当に不明である。  
何故かと言うと、これら解析情報はもともとネットで拾ったものだが、記事が2010年のもので、天則は2011年に1.10aへとアップデートされているため、その時点での情報はすでに使えない可能性がある。  
その情報によれば、送信回数を5で割ったものに初期化時に決めた乱数を足したり足さなかったりしていたらしい。  
`log1.txt`や`log2.txt`を見る限り、今は割り算ではないような気がする。(1ずつ増えているので)  
**というわけで現在のバージョンではこの部分が未解析のため、正常に動かない。**