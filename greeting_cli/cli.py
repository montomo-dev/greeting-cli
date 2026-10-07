import argparse
import sys

DEFAULT_NAME = "World"
MAX_NAME_LENGTH = 100


def build_greeting(name, shout=False):
    """Return a greeting for ``name``.

    Surrounding whitespace is trimmed; a blank name raises ``ValueError``.
    """
    cleaned = " ".join(name.split())
    if not cleaned:
        raise ValueError("name must not be empty")
    if len(cleaned) > MAX_NAME_LENGTH:
        raise ValueError(f"name must be at most {MAX_NAME_LENGTH} characters")
    greeting = f"Hello, {cleaned}! Nice to meet you."
    return greeting.upper() if shout else greeting


def build_parser():
    parser = argparse.ArgumentParser(
        prog="greeting-cli",
        description="Print a friendly greeting.",
    )
    parser.add_argument(
        "name",
        nargs="*",
        help=f"name to greet (default: {DEFAULT_NAME})",
    )
    parser.add_argument(
        "-s",
        "--shout",
        action="store_true",
        help="print the greeting in upper case",
    )
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    name = " ".join(args.name) if args.name else DEFAULT_NAME
    try:
        print(build_greeting(name, shout=args.shout))
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 0
