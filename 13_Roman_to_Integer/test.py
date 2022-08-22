import unittest
r2i = __import__('13_Roman_to_Integer')

class MyTestCase(unittest.TestCase):
    converter2 = r2i.Roman2Int()

    def test(self):
        converter2 = r2i.Roman2Int()
        self.assertEqual(converter2.convert("I"), 1)

    def test2(self):
        converter2 = r2i.Roman2Int()
        self.assertEqual(converter2.convert("LVIII"), 58)

    def test3(self):
        converter2 = r2i.Roman2Int()
        self.assertEqual(converter2.convert("MCMXCIV"), 1994)


if __name__ == '__main__':
    unittest.main()
