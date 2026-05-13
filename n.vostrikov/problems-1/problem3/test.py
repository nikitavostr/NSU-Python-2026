import unittest
from io import StringIO
from unittest.mock import patch

from problem3 import collatz, main


class TestCollatz(unittest.TestCase):
    def test_1(self):
        self.assertEqual(collatz(1), [1])

    def test_7(self):
        self.assertEqual(
            collatz(7),
            [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        )

    def test_10(self):
        self.assertEqual(
            collatz(10),
            [10, 5, 16, 8, 4, 2, 1]
        )

    def test_19(self):
        self.assertEqual(
            collatz(19),
            [19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        )

    def test_zero(self):
        self.assertEqual(collatz(0), [])

    def test_negative(self):
        self.assertEqual(collatz(-4), [])


class TestMain(unittest.TestCase):
    def test_main_7(self):
        with patch("builtins.input", return_value="7"), \
             patch("sys.stdout", new=StringIO()) as out:
            main()
            self.assertEqual(
                out.getvalue(),
                "7->22->11->34->17->52->26->13->40->20->10->5->16->8->4->2->1\n"
            )

    def test_main_10(self):
        with patch("builtins.input", return_value="10"), \
             patch("sys.stdout", new=StringIO()) as out:
            main()
            self.assertEqual(out.getvalue(), "10->5->16->8->4->2->1\n")

    def test_main_with_spaces(self):
        with patch("builtins.input", return_value="   19   "), \
             patch("sys.stdout", new=StringIO()) as out:
            main()
            self.assertEqual(
                out.getvalue(),
                "19->58->29->88->44->22->11->34->17->52->26->13->40->20->10->5->16->8->4->2->1\n"
            )

    def test_main_invalid_input(self):
        with patch("builtins.input", return_value="abc"):
            with self.assertRaises(ValueError):
                main()


if __name__ == "__main__":
    unittest.main()
