# greeting-cli

名前を受け取って、挨拶を表示する小さなコマンドラインプログラムです。Python 3 の標準ライブラリだけで動きます。

## 使い方

```bash
python3 greeting.py 太郎                  # こんにちは、太郎さん！
python3 greeting.py Alice --lang en       # Hello, Alice!
python3 greeting.py Alice --lang en --shout   # HELLO, ALICE!
```

| オプション | 内容 |
|------------|------|
| `--lang ja\|en` | 言語。既定は `ja` |
| `--shout` | 大文字で表示する(英語向け) |

名前が空のときは、エラーメッセージを標準エラーに出して終了コード 1 を返します。

## テスト

```bash
python3 -m unittest discover -s tests
```
