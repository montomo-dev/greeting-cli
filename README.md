# greeting-cli

名前を受け取って、あいさつを表示する小さなコマンドラインプログラムです。
Python 3.8 以上の標準ライブラリだけで動きます(インストール不要)。

## 使い方

```bash
python -m greeting_cli Alice
# Hello, Alice! Nice to meet you.

python -m greeting_cli Alice Smith     # 複数語の名前もOK
python -m greeting_cli                 # 名前なし → Hello, World! ...
python -m greeting_cli --shout bob     # HELLO, BOB! NICE TO MEET YOU.
python -m greeting_cli --help
```

空白だけの名前や 100 文字を超える名前はエラー(終了コード 2)になります。

## テスト

```bash
python -m unittest discover -v
```

## 構成

- `greeting_cli/cli.py` — あいさつ生成(`build_greeting`)と引数処理(`main`)
- `greeting_cli/__main__.py` — `python -m greeting_cli` の入口
- `tests/test_cli.py` — テスト
