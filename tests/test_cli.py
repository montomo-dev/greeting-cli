import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from greeting_cli.cli import MAX_NAME_LENGTH, build_greeting, main


def run(argv):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        code = main(argv)
    return code, out.getvalue(), err.getvalue()


class BuildGreetingTest(unittest.TestCase):
    def test_greets_by_name(self):
        self.assertEqual(build_greeting("Alice"), "Hello, Alice! Nice to meet you.")

    def test_collapses_extra_whitespace(self):
        self.assertEqual(build_greeting("  Alice   Smith "), "Hello, Alice Smith! Nice to meet you.")

    def test_supports_non_ascii_names(self):
        self.assertEqual(build_greeting("太郎"), "Hello, 太郎! Nice to meet you.")

    def test_shout_uppercases(self):
        self.assertEqual(build_greeting("bob", shout=True), "HELLO, BOB! NICE TO MEET YOU.")

    def test_blank_name_is_rejected(self):
        for blank in ("", "   ", "\t\n"):
            with self.assertRaises(ValueError):
                build_greeting(blank)

    def test_too_long_name_is_rejected(self):
        with self.assertRaises(ValueError):
            build_greeting("a" * (MAX_NAME_LENGTH + 1))
        build_greeting("a" * MAX_NAME_LENGTH)


class MainTest(unittest.TestCase):
    def test_prints_greeting(self):
        code, out, err = run(["Alice"])
        self.assertEqual((code, out, err), (0, "Hello, Alice! Nice to meet you.\n", ""))

    def test_joins_multiple_words(self):
        code, out, _ = run(["Alice", "Smith"])
        self.assertEqual((code, out), (0, "Hello, Alice Smith! Nice to meet you.\n"))

    def test_defaults_to_world(self):
        code, out, _ = run([])
        self.assertEqual((code, out), (0, "Hello, World! Nice to meet you.\n"))

    def test_shout_flag(self):
        code, out, _ = run(["--shout", "bob"])
        self.assertEqual((code, out), (0, "HELLO, BOB! NICE TO MEET YOU.\n"))

    def test_blank_name_exits_with_error(self):
        code, out, err = run(["   "])
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertIn("name must not be empty", err)


if __name__ == "__main__":
    unittest.main()
