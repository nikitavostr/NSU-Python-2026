import unittest

from problem4 import sing_the_song


class TestSingTheSong(unittest.TestCase):
    def test_sing_the_song(self) -> None:
        expected = (
            "Ten green bottles hanging on the wall,\n"
            "Ten green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be nine green bottles hanging on the wall.\n"
            "Nine green bottles hanging on the wall,\n"
            "Nine green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be eight green bottles hanging on the wall.\n"
            "Eight green bottles hanging on the wall,\n"
            "Eight green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be seven green bottles hanging on the wall.\n"
            "Seven green bottles hanging on the wall,\n"
            "Seven green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be six green bottles hanging on the wall.\n"
            "Six green bottles hanging on the wall,\n"
            "Six green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be five green bottles hanging on the wall.\n"
            "Five green bottles hanging on the wall,\n"
            "Five green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be four green bottles hanging on the wall.\n"
            "Four green bottles hanging on the wall,\n"
            "Four green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be three green bottles hanging on the wall.\n"
            "Three green bottles hanging on the wall,\n"
            "Three green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be two green bottles hanging on the wall.\n"
            "Two green bottles hanging on the wall,\n"
            "Two green bottles hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            "There'll be one green bottle hanging on the wall.\n"
            "One green bottle hanging on the wall,\n"
            "One green bottle hanging on the wall,\n"
            "If that one green bottle should accidentally fall,\n"
            "There'll be no green bottles hanging on the wall."
        )
        self.assertEqual("\n".join(sing_the_song()), expected)


if __name__ == "__main__":
    unittest.main()
