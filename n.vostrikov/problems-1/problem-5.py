import unittest

def prime_factorization(n: int) -> list[list[int]]:
    if n < 1:
        raise ValueError("n must be positive")
    result = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            result.append([i, cnt])
        i += 1
    if n != 1:
        result.append([n, 1])
    return result

class TestPrimeFactorization(unittest.TestCase):
    def test_1(self):
        self.assertEqual(prime_factorization(1), [])

    def test_prime_number(self):
        self.assertEqual(prime_factorization(47), [[47, 1]])

    def test_complex_number(self):
        self.assertEqual(prime_factorization(120), [[2, 3], [3, 1], [5, 1]])

    def test_non_positive_number(self):
        with self.assertRaises(ValueError):
            prime_factorization(-10)


if __name__ == "__main__":
    unittest.main()