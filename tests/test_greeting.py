import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

import greeting


class BuildGreetingTest(unittest.TestCase):
    def test_default_is_japanese(self):
        self.assertEqual(greeting.build_greeting("太郎"), "こんにちは、太郎さん！")

    def test_english(self):
        self.assertEqual(greeting.build_greeting("Alice", lang="en"), "Hello, Alice!")

    def test_shout_uppercases(self):
        self.assertEqual(greeting.build_greeting("Alice", lang="en", shout=True), "HELLO, ALICE!")

    def test_name_is_stripped(self):
        self.assertEqual(greeting.build_greeting("  Bob  ", lang="en"), "Hello, Bob!")

    def test_blank_name_rejected(self):
        for blank in ("", "   "):
            with self.assertRaises(ValueError):
                greeting.build_greeting(blank)

    def test_unknown_language_rejected(self):
        with self.assertRaises(ValueError):
            greeting.build_greeting("Alice", lang="fr")


class MainTest(unittest.TestCase):
    def run_main(self, argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = greeting.main(argv)
        return code, out.getvalue(), err.getvalue()

    def test_prints_greeting(self):
        code, out, _ = self.run_main(["Alice", "--lang", "en"])
        self.assertEqual((code, out), (0, "Hello, Alice!\n"))

    def test_blank_name_exits_with_error(self):
        code, out, err = self.run_main([" "])
        self.assertEqual(code, 1)
        self.assertEqual(out, "")
        self.assertIn("エラー", err)

    def test_invalid_lang_is_rejected_by_argparse(self):
        with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as cm:
            greeting.parse_args(["Alice", "--lang", "fr"])
        self.assertEqual(cm.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
