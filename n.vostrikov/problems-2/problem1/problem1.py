import unittest

def pythagorean_triples(n: int) -> list[tuple[int, int, int]]:
    return [
        (x, y, z)
        for x in range(1, n + 1)
        for y in range(x + 1, n + 1)
        for z in range(y + 1, n + 1)
        if x ** 2 + y ** 2 == z ** 2
    ]


class TestPythagoreanTriples(unittest.TestCase):
    def test_n_5(self) -> None:
        self.assertEqual(pythagorean_triples(5), [(3, 4, 5)])

    def test_n_less_than_5(self) -> None:
        self.assertEqual(pythagorean_triples(4), [])
        self.assertEqual(pythagorean_triples(1), [])
        self.assertEqual(pythagorean_triples(0), [])

    def test_negative_n(self) -> None:
        self.assertEqual(pythagorean_triples(-10), [])

    def test_n_15(self) -> None:
        self.assertEqual(
            pythagorean_triples(15),
            [(3, 4, 5), (5, 12, 13), (6, 8, 10), (9, 12, 15)],
        )

    def test_order(self) -> None:
        for x, y, z in pythagorean_triples(30):
            self.assertLess(x, y)
            self.assertLess(y, z)

    def test_pythagorean_identity(self) -> None:
        for x, y, z in pythagorean_triples(100):
            self.assertEqual(x ** 2 + y ** 2, z ** 2)

if __name__ == "__main__":
    unittest.main()

