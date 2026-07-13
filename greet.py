#!/usr/bin/env python3
"""A tiny command-line program that prints a friendly greeting."""
from __future__ import annotations

import argparse


def build_greeting(name: str, greeting: str = "Hello") -> str:
    """Return a friendly greeting for ``name``.

    Empty or whitespace-only names fall back to "friend".
    """
    name = name.strip()
    if not name:
        name = "friend"
    return f"{greeting}, {name}! Nice to meet you."


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument(
        "name",
        nargs="?",
        default="friend",
        help="Name to greet (default: friend)",
    )
    parser.add_argument(
        "-g",
        "--greeting",
        default="Hello",
        help='Greeting word to use (default: "Hello")',
    )
    args = parser.parse_args(argv)
    print(build_greeting(args.name, args.greeting))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
