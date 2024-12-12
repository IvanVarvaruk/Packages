import unittest
from reverse_words.src import reverse_words

class TestReverseWords(unittest.TestCase):

    def test_reverse_words(self):
        self.assertEqual(reverse_words("hello"), "olleh")
        self.assertEqual(reverse_words("hello world"), "olleh dlrow")
        self.assertEqual(reverse_words("a1bcd efg!h"), "d1cba hgf!e")
        self.assertEqual(reverse_words("123"), "123")
        self.assertEqual(reverse_words(""), "")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            reverse_words(12345)

if __name__ == "__main__":
    unittest.main()
