import subprocess
import sys
import unittest
from pathlib import Path

from greet import build_greeting


ROOT = Path(__file__).resolve().parent
GREET = ROOT / "greet.py"


class GreetingTests(unittest.TestCase):
    def test_build_greeting_with_name(self):
        self.assertEqual(
            build_greeting("Ada"),
            "Hello, Ada! Nice to meet you.",
        )

    def test_build_greeting_trims_whitespace(self):
        self.assertEqual(
            build_greeting("  Grace  "),
            "Hello, Grace! Nice to meet you.",
        )

    def test_build_greeting_defaults_blank_name_to_friend(self):
        self.assertEqual(
            build_greeting("   "),
            "Hello, friend! Nice to meet you.",
        )

    def test_cli_prints_greeting(self):
        result = subprocess.run(
            [sys.executable, str(GREET), "Linus"],
            check=True,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.stdout.strip(), "Hello, Linus! Nice to meet you.")

    def test_cli_supports_custom_greeting(self):
        result = subprocess.run(
            [sys.executable, str(GREET), "--greeting", "Hi", "Kota"],
            check=True,
            text=True,
            capture_output=True,
        )
        self.assertEqual(result.stdout.strip(), "Hi, Kota! Nice to meet you.")


if __name__ == "__main__":
    unittest.main()
