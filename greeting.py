"""名前を受け取って挨拶を表示する小さなコマンドラインプログラム。"""

import argparse
import sys

GREETINGS = {
    "ja": "こんにちは、{name}さん！",
    "en": "Hello, {name}!",
}


def build_greeting(name: str, lang: str = "ja", shout: bool = False) -> str:
    """挨拶文を組み立てる。名前が空(空白のみ含む)なら ValueError。"""
    name = name.strip()
    if not name:
        raise ValueError("名前が空です")
    if lang not in GREETINGS:
        raise ValueError(f"未対応の言語です: {lang}")
    message = GREETINGS[lang].format(name=name)
    return message.upper() if shout else message


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="名前を受け取って挨拶を表示します。")
    parser.add_argument("name", help="挨拶する相手の名前")
    parser.add_argument("--lang", choices=sorted(GREETINGS), default="ja", help="言語(既定: ja)")
    parser.add_argument("--shout", action="store_true", help="大文字で表示する(英語向け)")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    try:
        print(build_greeting(args.name, args.lang, args.shout))
    except ValueError as e:
        print(f"エラー: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
